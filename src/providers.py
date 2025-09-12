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
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        
        # 세션 사용으로 안정성 향상
        session = requests.Session()
        session.headers.update(headers)
        
        response = session.get(url, timeout=15)
        response.raise_for_status()
        
        print(f"[DEBUG] Wevity response status: {response.status_code}")
        print(f"[DEBUG] Wevity response length: {len(response.text)}")
        
        soup = BeautifulSoup(response.text, "html.parser")
        contests = []

        # 다양한 셀렉터 시도
        selectors = [
            ".list li",
            "ul.list li", 
            ".contest_list li",
            "li[class*='list']",
            ".item",
            "tr"
        ]
        
        contest_items = []
        for selector in selectors:
            items = soup.select(selector)
            if items and len(items) > 1:
                print(f"[DEBUG] Found {len(items)} items with selector: {selector}")
                contest_items = items[1:] if selector in [".list li", "ul.list li"] else items
                break
        
        if not contest_items:
            print("[WARNING] No contest items found with any selector")
            # HTML 구조 디버깅
            print(f"[DEBUG] Page title: {soup.find('title').text if soup.find('title') else 'No title'}")
            return []
        
        for item in contest_items[:50]:  # 최대 50개만 처리
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
                
                # 제목에서 불필요한 부분 제거
                if "SPECIAL" in title:
                    title = title.split("SPECIAL")[0].strip()
                
                # 유효한 공모전인지 확인
                if title and link and len(title) > 5 and "공모전" in title:
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

def fetch_onbid():
    """온비드 공모전 크롤링"""
    url = "https://www.onbid.co.kr/op/ctt/cttList.do"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5",
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        contests = []

        # 온비드의 공모전 목록 구조
        contest_items = soup.select("tbody tr") or soup.select(".list tr") or soup.select("table tr")
        
        for item in contest_items:
            try:
                # 제목과 링크 찾기
                title_el = item.select_one("a") or item.select_one("td a")
                if not title_el:
                    continue
                    
                title = title_el.get_text(strip=True)
                link = title_el.get("href", "")
                
                if link and not link.startswith("http"):
                    link = "https://www.onbid.co.kr" + link
                
                # 공모전 관련 키워드가 포함된 것만
                if title and link and len(title) > 5 and any(keyword in title for keyword in ['공모전', '대회', '콘테스트', '경진대회']):
                    contests.append({
                        "title": title,
                        "url": link,
                        "site": "OnBid",
                        "start_date": None,
                        "end_date": None
                    })
            except Exception as e:
                continue

        print(f"[INFO] fetch_onbid fetched {len(contests)} items")
        return contests
        
    except Exception as e:
        print(f"[ERROR] fetch_onbid failed: {e}")
        return []

def fetch_all_contest():
    """올콘테스트 공모전 크롤링 - 현재 도메인 접근 불가로 비활성화"""
    print("[WARNING] AllContest domain is currently unavailable")
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
