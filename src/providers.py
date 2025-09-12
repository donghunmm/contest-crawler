import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_linkareer():
    """Linkareer 공모전 크롤링 - 현재 서버 응답 문제로 비활성화"""
    print("[WARNING] Linkareer is currently unavailable (server timeout)")
    return []

def fetch_campuspick():
    """CampusPick 공모전 크롤링 - JavaScript 동적 로딩으로 인해 현재 비활성화"""
    print("[WARNING] CampusPick requires JavaScript rendering, currently unavailable")
    return []

def fetch_wevity():
    """위비티 공모전 크롤링"""
    url = "https://www.wevity.com/?c=find&s=1&gub=1"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        contests = []

        # 위비티의 공모전 목록 구조 (.list li 사용)
        contest_items = soup.select(".list li")[1:]  # 첫 번째는 헤더이므로 제외
        
        for item in contest_items:
            try:
                # 제목과 링크 찾기
                link_el = item.select_one("a")
                if not link_el:
                    continue
                    
                title = link_el.get_text(strip=True)
                link = link_el.get("href", "")
                
                # 상대 경로를 절대 경로로 변환
                if link and not link.startswith("http"):
                    if link.startswith("?"):
                        link = "https://www.wevity.com/" + link
                    else:
                        link = "https://www.wevity.com/" + link
                
                # 제목에서 불필요한 부분 제거 (SPECIAL, 분야 정보 등)
                if "SPECIAL" in title:
                    title = title.split("SPECIAL")[0].strip()
                
                # 유효한 공모전인지 확인
                if title and link and len(title) > 5:
                    contests.append({
                        "title": title,
                        "url": link,
                        "site": "Wevity",
                        "start_date": None,
                        "end_date": None
                    })
            except Exception as e:
                continue

        print(f"[INFO] fetch_wevity fetched {len(contests)} items")
        return contests
        
    except Exception as e:
        print(f"[ERROR] fetch_wevity failed: {e}")
        return []

def fetch_thinkcontest():
    """씽크콘테스트 공모전 크롤링 - JavaScript 동적 로딩으로 현재 비활성화"""
    print("[WARNING] ThinkContest requires JavaScript rendering, currently unavailable")
    return []

def fetch_all_contest():
    """올콘테스트 공모전 크롤링"""
    url = "http://www.allcontest.co.kr/contest/contest.asp"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'euc-kr'  # 한국 사이트 인코딩
        soup = BeautifulSoup(response.text, "html.parser")
        contests = []

        # 테이블 구조에서 공모전 정보 추출
        rows = soup.select("table tr")
        
        for row in rows:
            try:
                cells = row.find_all('td')
                if len(cells) >= 2:
                    # 제목과 링크 찾기
                    title_cell = cells[1] if len(cells) > 1 else cells[0]
                    link_el = title_cell.find('a')
                    
                    if link_el:
                        title = link_el.get_text(strip=True)
                        link = link_el.get("href", "")
                        
                        if link and not link.startswith("http"):
                            link = "http://www.allcontest.co.kr" + link
                        
                        if title and link and len(title) > 5:
                            contests.append({
                                "title": title,
                                "url": link,
                                "site": "AllContest",
                                "start_date": None,
                                "end_date": None
                            })
            except Exception as e:
                continue

        print(f"[INFO] fetch_all_contest fetched {len(contests)} items")
        return contests
        
    except Exception as e:
        print(f"[ERROR] fetch_all_contest failed: {e}")
        return []

def fetch_contestkorea():
    """컨테스트코리아 공모전 크롤링"""
    url = "http://www.contestkorea.com/sub/list.php"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        contests = []

        # 컨테스트코리아의 공모전 목록 구조 분석
        contest_items = soup.select("table tr") or soup.select(".list tr")
        
        for item in contest_items[1:]:  # 첫 번째는 헤더일 가능성
            try:
                # 제목과 링크 찾기
                title_el = item.select_one("a") or item.select_one("td a")
                if not title_el:
                    continue
                    
                title = title_el.get_text(strip=True)
                link = title_el.get("href", "")
                
                # FAQ나 가이드 페이지 제외
                if any(exclude in title.lower() for exclude in ['faq', '가이드', '질문', '답변', '세금', '생활기록부', '입상하지 못한']):
                    continue
                
                if link and not link.startswith("http"):
                    link = "http://www.contestkorea.com" + link
                
                if title and link and len(title) > 5:
                    contests.append({
                        "title": title,
                        "url": link,
                        "site": "ContestKorea",
                        "start_date": None,
                        "end_date": None
                    })
            except Exception as e:
                continue

        print(f"[INFO] fetch_contestkorea fetched {len(contests)} items")
        return contests
        
    except Exception as e:
        print(f"[ERROR] fetch_contestkorea failed: {e}")
        return []
