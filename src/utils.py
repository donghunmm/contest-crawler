import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "contests.csv")
JSON_PATH = os.path.join(DATA_DIR, "contests.json")
KEYWORDS = ["AI 공모전", "개인정보 공모전", "SW", "공모전", "인공지능공모전"]
