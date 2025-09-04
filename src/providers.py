import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_linkareer():
    url = "https://linkareer.com/contest"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    contests = []

    for item in soup.select(".contest-item"):
        title_el = item.select_one(".contest-title")
        link_el = item.select_one("a")
        if not title_el or not link_el:
            continue
        title = title_el.get_text(strip=True)
        link = link_el["href"]
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
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    contests = []

    for item in soup.select(".contest-item"):
        title_el = item.select_one(".contest-title")
        link_el = item.select_one("a")
        if not title_el or not link_el:
            continue
        title = title_el.get_text(strip=True)
        link = link_el["href"]
        site = "Singood"
        start_date = None
        end_date = None

        contests.append({
            "title": title,
            "url": link,
            "site": site,
            "start_date": start_date,
            "end_date": end_date
        })

    print(f"[INFO] fetch_singood fetched {len(contests)} items")
    return contests

def fetch_campuspick():
    url = "https://campuspick.com/contest"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    contests = []

    for item in soup.select(".contest-item"):
        title_el = item.select_one(".contest-title")
        link_el = item.select_one("a")
        if not title_el or not link_el:
            continue
        title = title_el.get_text(strip=True)
        link = link_el["href"]
        site = "CampusPick"
        start_date = None
        end_date = None

        contests.append({
            "title": title,
            "url": link,
            "site": site,
            "start_date": start_date,
            "end_date": end_date
        })

    print(f"[INFO] fetch_campuspick fetched {len(contests)} items")
    return contests

def fetch_wibity():
    url = "https://wibity.com/contest"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    contests = []

    for item in soup.select(".contest-item"):
        title_el = item.select_one(".contest-title")
        link_el = item.select_one("a")
        if not title_el or not link_el:
            continue
        title = title_el.get_text(strip=True)
        link = link_el["href"]
        site = "Wibity"
        start_date = None
        end_date = None

        contests.append({
            "title": title,
            "url": link,
            "site": site,
            "start_date": start_date,
            "end_date": end_date
        })

    print(f"[INFO] fetch_wibity fetched {len(contests)} items")
    return contests
