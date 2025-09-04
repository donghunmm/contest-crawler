import requests
from bs4 import BeautifulSoup

def fetch_linkareer():
    url = "https://linkareer.com/contest"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    contests = []
    for div in soup.select(".contest-item"):
        contests.append({
            "title": div.select_one(".title").get_text(strip=True),
            "url": div.select_one("a")["href"],
            "site": "Linkareer",
            "start_date": None,
            "end_date": None
        })
    return contests

def fetch_singood():
    url = "https://www.singood.com/contest"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    contests = []
    for div in soup.select(".contest-item"):
        contests.append({
            "title": div.select_one(".title").get_text(strip=True),
            "url": div.select_one("a")["href"],
            "site": "Singood",
            "start_date": None,
            "end_date": None
        })
    return contests

def fetch_campuspick():
    url = "https://www.campuspick.com/contest"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    contests = []
    for div in soup.select(".contest-item"):
        contests.append({
            "title": div.select_one(".title").get_text(strip=True),
            "url": div.select_one("a")["href"],
            "site": "CampusPick",
            "start_date": None,
            "end_date": None
        })
    return contests

def fetch_wibity():
    url = "https://www.wibity.com/contest"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    contests = []
    for div in soup.select(".contest-item"):
        contests.append({
            "title": div.select_one(".title").get_text(strip=True),
            "url": div.select_one("a")["href"],
            "site": "Wibity",
            "start_date": None,
            "end_date": None
        })
    return contests
