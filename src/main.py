import json
import pandas as pd
import os
from .utils import DATA_DIR, CSV_PATH, JSON_PATH, KEYWORDS
from . import providers

PROVIDERS = [
    providers.fetch_example_site,
]

def filter_by_keywords(contests):
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
            all_contests.extend(fetcher())
        except Exception as e:
            print("[ERROR] provider failed:", fetcher.__name__, e)

    filtered = filter_by_keywords(all_contests)

    # 저장
    df = pd.DataFrame(filtered)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    print(f"[INFO] {len(filtered)} contests saved")

if __name__ == "__main__":
    run()
