import pytest
from datetime import datetime
from pathlib import Path
import sys

# 📂 tests/📊test-reports📊 폴더에 저장
BASE_DIR = Path(__file__).resolve().parent
report_dir = BASE_DIR / "📊test-reports📊"

# 폴더 없으면 자동 생성
report_dir.mkdir(parents=True, exist_ok=True)

# 파일명: report_YYYY-MM-DD_HH-MM-SS.html
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = report_dir / f"report_{timestamp}.html"

# 명령줄에서 스크립트 이름(sys.argv[0])을 제외한 나머지 인자들을 가져옴
args = [
    f'--html={filename}',
    '--self-contained-html',
    '--log-cli-level=INFO'
] + sys.argv[1:]

# pytest.main() 함수로 pytest 실행
pytest.main(args)