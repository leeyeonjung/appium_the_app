import pytest
from datetime import datetime
import sys

# 현재 날짜와 시간을 가져와 'YYYY-MM-DD_HH-MM-SS' 형식으로 포맷
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"report_{timestamp}.html"

# 명령줄에서 스크립트 이름(sys.argv[0])을 제외한 나머지 인자들을 가져옴
args = [
    f'--html={filename}',
    '--self-contained-html',
    '--log-cli-level=INFO'
] + sys.argv[1:]


# pytest.main() 함수로 pytest 실행
# 명령줄 인자들이 'args' 변수를 통해 pytest에 전달됨
pytest.main(args)


# pytest 명령어 전체 내용 실행 : python run_tests.py
# 특정 파일 : python run_tests.py testcase/test_login.py
# 특정 파일의 함수만 실행: python run_tests.py testcase/test_login.py::test_setup
# marker 표시된 내용만 실행 : python run_tests.py -m "smoke"
# log 정보 출력 : python run_tests.py --log-cli-level=INFO