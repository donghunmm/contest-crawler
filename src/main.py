import json
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import DATA_DIR, CSV_PATH, JSON_PATH, KEYWORDS
import providers
import test_providers

PROVIDERS = [
    test_providers.fetch_test_data,  # 테스트용 데이터
    providers.fetch_wevity,
    providers.fetch_gongmo,
    providers.fetch_contestkorea,
    # providers.fetch_onbid,  # 접근 불가로 비활성화
    # providers.fetch_all_contest,  # 도메인 접근 불가로 비활성화
    # providers.fetch_thinkcontest,  # JavaScript 렌더링 필요로 비활성화
    # providers.fetch_linkareer,  # 현재 서버 문제로 비활성화
    # providers.fetch_campuspick,  # JavaScript 렌더링 필요로 비활성화
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
            fetched = fetcher()
            all_contests.extend(fetched)
        except Exception as e:
            print("[ERROR] provider failed:", fetcher.__name__, e)

    filtered = filter_by_keywords(all_contests)
    print(f"[INFO] {len(filtered)} contests matched keywords")

    df = pd.DataFrame(filtered)
    df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Data saved to {CSV_PATH} and {JSON_PATH}")

if __name__ == "__main__":
    run()
