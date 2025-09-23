import pytest
import os
from datetime import datetime
import sys

# 리포트 저장 폴더
report_dir = "📊test-reports📊"
os.makedirs(report_dir, exist_ok=True)  # 폴더 없으면 자동 생성

# 현재 날짜와 시간을 가져와 'YYYY-MM-DD_HH-MM-SS' 형식으로 포맷
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = os.path.join(report_dir, f"report_{timestamp}.html")

# 명령줄에서 스크립트 이름(sys.argv[0])을 제외한 나머지 인자들을 가져옴
args = [
    f'--html={filename}',
    '--self-contained-html',
    '--log-cli-level=DEBUG'
] + sys.argv[1:]

# pytest.main() 함수로 pytest 실행
pytest.main(args)