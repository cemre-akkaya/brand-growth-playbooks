import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

APIFY_TOKEN = os.environ.get('APIFY_TOKEN', '')

def scrape_website(url):
    print(f"[*] Scraping website: {url}")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"[!] Error fetching website: {e}")
        return {}

    soup = BeautifulSoup(html, 'html.parser')
    
    # Metadata
    title = soup.title.string.strip() if soup.title else ""
    meta_desc = ""
    desc_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
    if desc_tag and desc_tag.get('content'):
        meta_desc = desc_tag['content'].strip()
        
    # Headings
    h1s = [h.get_text(strip=True) for h in soup.find_all('h1')]
    h2s = [h.get_text(strip=True) for h in soup.find_all('h2')][:10]
    
    # Schema JSON-LD
    schemas = []
    for s in soup.find_all('script', type='application/ld+json'):
        try:
            schemas.append(json.loads(s.string))
        except Exception:
            pass

    # Shopify check
    is_shopify = 'cdn.shopify.com' in html or 'Shopify.theme' in html
    shopify_products = []
    if is_shopify:
        try:
            base_url = urllib.parse.urljoin(url, '/products.json?limit=5')
            req_p = urllib.request.Request(base_url, headers=headers)
            with urllib.request.urlopen(req_p, timeout=5) as p_resp:
                p_data = json.loads(p_resp.read().decode('utf-8'))
                shopify_products = [
                    {
                        'title': p.get('title'),
                        'handle': p.get('handle'),
                        'price': p.get('variants', [{}])[0].get('price'),
                        'tags': p.get('tags')
                    }
                    for p in p_data.get('products', [])
                ]
        except Exception:
            pass

    return {
        'url': url,
        'title': title,
        'meta_description': meta_desc,
        'is_shopify': is_shopify,
        'h1_headings': h1s,
        'h2_headings': h2s,
        'schemas_found': len(schemas),
        'sample_products': shopify_products
    }

def scrape_reddit_sentiment(keyword, limit=10):
    print(f"[*] Querying Reddit sentiment for: '{keyword}' via Apify...")
    if not APIFY_TOKEN:
        print("[!] No Apify token configured.")
        return []
        
    # Apify Reddit Scraper Lite endpoint
    actor_id = 'trudax~reddit-scraper-lite'
    run_url = f"https://api.apify.com/v2/acts/{actor_id}/run-sync-get-dataset-items?token={APIFY_TOKEN}"
    
    payload = json.dumps({
        "searches": [keyword],
        "sort": "relevance",
        "time": "year",
        "maxItems": limit,
        "type": "post"
    }).encode('utf-8')
    
    req = urllib.request.Request(run_url, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            items = json.loads(resp.read().decode('utf-8'))
            results = []
            for it in items:
                results.append({
                    'title': it.get('title'),
                    'subreddit': it.get('subreddit'),
                    'score': it.get('score'),
                    'numComments': it.get('numComments'),
                    'url': it.get('url'),
                    'body': (it.get('body') or '')[:500]
                })
            print(f"[+] Retrieved {len(results)} Reddit threads successfully.")
            return results
    except Exception as e:
        print(f"[!] Apify Reddit query note: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Automated Brand Intelligence & Data Dossier Extractor")
    parser.add_argument("--brand", required=True, help="Brand Name")
    parser.add_argument("--url", required=True, help="Brand Website URL")
    parser.add_argument("--reddit_keyword", help="Niche keyword to search Reddit for VoC")
    parser.add_argument("--output", default="brand_dossier.json", help="Output file path")
    args = parser.parse_args()

    dossier = {
        'brand': args.brand,
        'website_data': scrape_website(args.url),
        'reddit_voc_data': scrape_reddit_sentiment(args.reddit_keyword) if args.reddit_keyword else []
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(dossier, f, indent=2, ensure_ascii=False)

    print(f"\n[✓] Brand Dossier successfully built and saved to: {args.output}")

if __name__ == '__main__':
    main()
