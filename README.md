# Contest Crawler 🏆

한국의 주요 공모전 사이트들에서 공모전 정보를 자동으로 수집하는 크롤러입니다.

## 📋 기능

- **자동 크롤링**: 매일 자동으로 최신 공모전 정보 수집
- **키워드 필터링**: AI, SW, 개인정보 등 관심 키워드로 필터링
- **다중 사이트 지원**: 여러 공모전 사이트에서 데이터 수집
- **데이터 저장**: JSON 및 CSV 형태로 결과 저장

## 🎯 지원 사이트

- **Wevity** (위비티) - 주요 데이터 소스
- **ContestKorea** (컨테스트코리아)
- ~~Linkareer~~ (현재 서버 문제로 비활성화)
- ~~CampusPick~~ (JavaScript 렌더링 필요로 비활성화)

## 🔍 키워드 필터링

다음 키워드가 포함된 공모전만 수집합니다:
- AI 공모전
- 개인정보 공모전  
- SW
- 공모전
- 인공지능공모전

## 📊 데이터 형식

수집된 데이터는 다음 형태로 저장됩니다:

```json
{
  "title": "공모전 제목",
  "url": "공모전 링크",
  "site": "출처 사이트",
  "start_date": null,
  "end_date": null
}
```

## 🚀 사용법

### 로컬 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 크롤러 실행
python src/main.py
```

### GitHub Actions 설정

#### 1. Repository Secrets 설정
Settings > Secrets and variables > Actions에서 다음 시크릿을 설정하세요:

```
EMAIL_USERNAME: 발송용 Gmail 주소 (예: your-email@gmail.com)
EMAIL_PASSWORD: Gmail 앱 비밀번호
EMAIL_TO: 수신할 이메일 주소 (예: recipient@gmail.com)
```

#### 2. Gmail 앱 비밀번호 생성
1. Google 계정 > 보안 > 2단계 인증 활성화
2. 앱 비밀번호 생성 (16자리 코드)
3. 생성된 비밀번호를 `EMAIL_PASSWORD`에 설정

#### 3. 자동 실행
- **스케줄**: 매일 오전 9시 (한국시간)
- **수동 실행**: GitHub Actions 탭에서 "Run workflow" 버튼으로 수동 실행 가능
- **이메일 알림**: 새로운 공모전이 발견되면 자동으로 이메일 발송
- **자동 커밋**: 새로운 데이터가 있으면 자동으로 커밋 및 푸시

## 📁 파일 구조

```
contest-crawler/
├── src/
│   ├── main.py          # 메인 실행 파일
│   ├── providers.py     # 각 사이트별 크롤링 로직
│   └── utils.py         # 유틸리티 함수 및 설정
├── data/
│   ├── contests.json    # JSON 형태 결과
│   └── contests.csv     # CSV 형태 결과
├── .github/workflows/
│   └── crawl-contests.yml # GitHub Actions 워크플로우
└── requirements.txt     # Python 의존성
```

## 🛠️ 기술 스택

- **Python 3.11+**
- **requests**: HTTP 요청
- **BeautifulSoup4**: HTML 파싱
- **pandas**: 데이터 처리 및 CSV 저장
- **GitHub Actions**: 자동화

## 📈 최근 업데이트

- ✅ Wevity 크롤링 안정화
- ✅ URL 형식 수정
- ✅ FAQ 페이지 필터링 추가
- ✅ GitHub Actions 자동화 설정
- ✅ 에러 처리 개선

## 🤝 기여하기

새로운 공모전 사이트 추가나 기능 개선에 대한 기여를 환영합니다!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request