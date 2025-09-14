import pytest
from datetime import datetime
import sys

# 현재 날짜와 시간을 가져와 'YYYY-MM-DD_HH-MM-SS' 형식으로 포맷
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"report_{timestamp}.html"

# 명령줄에서 스크립트 이름(sys.argv[0])을 제외한 나머지 인자들을 가져옴
args = [f'--html={filename}', '--self-contained-html'] + sys.argv[1:]

# pytest.main() 함수로 pytest 실행
# 명령줄 인자들이 'args' 변수를 통해 pytest에 전달됨
pytest.main(args)