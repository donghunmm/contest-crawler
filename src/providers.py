import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_linkareer():
    url = "https://linkareer.com/contest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    contests = []

    for item in soup.select(".contest-item"):
        title = item.select_one(".contest-title").get_text(strip=True)
        link = item.select_one("a")["href"]
        site = "Linkareer"
        start_date = None
        end_date = None

        contests.append({
            "title": title,
            "url": link,
            "site": site,
            "start_date": start_date,
            "end_date": end_date
        })

    print(f"[INFO] fetch_linkareer fetched {len(contests)} items")
    return contests

def fetch_singood():
    url = "https://www.singood.co.kr/contest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    contests = []

    for item in soup.select(".contest-
