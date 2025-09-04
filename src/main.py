import json
import pandas as pd
import os
from .utils import DATA_DIR, CSV_PATH, JSON_PATH, KEYWORDS
from . import providers

# 실제 존재하는 크롤러 함수로 변경
PROVIDERS = [
    providers.fetch_linkareer,
    providers.fetch_singood,
    providers.fetch_campuspick,
    providers.fetch_wibity
]

def filter_by_keywords(contests):
    """제목에 키워드가 포함된 공모전만 필터링"""
    results = []
    for c in contests:
        if any(k.lower() in c["title"].lower() for k in KEYWORDS):
            results.append(c)
    return results

def run():
    os.makedirs(DATA_DIR, exist_ok=True)
    all_contests = []

    for fetcher in PROVIDERS:
        try:
            fetched = fetcher()
            print(f"[INFO] {fetcher.__name__} fetched {len(fetched)} items")
            all_contests.extend(fetched)
        except Exception as e:
            print("[ERROR] provider failed:", fetcher.__name__, e)

    filtered = filter_by_keywords(all_contests)
    print(f"[INFO] {len(filtered)} contests matched keywords")

    # CSV 저장
    df = pd.DataFrame(filtered)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    # JSON 저장
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Data saved to {CSV_PATH} and {JSON_PATH}")

if __name__ == "__main__":
    run()
