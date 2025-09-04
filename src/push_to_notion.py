import os
import json
import requests
from .utils import JSON_PATH

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def query_existing_pages():
    """기존 DB 페이지의 URL을 가져와서 중복 방지"""
    url = f"https://api.notion.com/v1/databases/{NOTION_DB_ID}/query"
    existing_urls = set()
    has_more = True
    payload = {}
    while has_more:
        r = requests.post(url, headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()
        for row in data["results"]:
            props = row.get("properties", {})
            page_url = props.get("URL", {}).get("url")
            if page_url:
                existing_urls.add(page_url)
        has_more = data.get("has_more", False)
        if has_more:
            payload["start_cursor"] = data["next_cursor"]
    return existing_urls

def create_page(item):
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {
            "Title": {"title": [{"text": {"content": item["title"]}}]},
            "Site": {"rich_text": [{"text": {"content": item.get("site", "")}}]},
            "URL": {"url": item["url"]},
        }
    }
    if item.get("start_date"):
        data["properties"]["Start Date"] = {"date": {"start": item["start_date"]}}
    if item.get("end_date"):
        data["properties"]["End Date"] = {"date": {"start": item["end_date"]}}

    r = requests.post(url, headers=headers, data=json.dumps(data))
    if r.status_code != 200:
        print("[ERROR]", r.text)
    else:
        print(f"[OK] Added to Notion: {item['title']}")

def run():
    if not os.path.exists(JSON_PATH):
        print("[WARN] contests.json not found")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    existing_urls = query_existing_pages()
    print(f"[INFO] Existing URLs in Notion: {len(existing_urls)}")

    for item in items:
        if item["url"] not in existing_urls:
            create_page(item)
        else:
            print(f"[SKIP] Already exists: {item['title']}")

if __name__ == "__main__":
    run()
