from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import warnings
# 결과가 xml형식으로 반환된다. 이것을 dict 로 바꿔주는 라이브러리이다.
import xmltodict 
## 필요한 라이브러리 임포트
import requests
import pprint
import json

warnings.filterwarnings('ignore')

# 초단기예보조회
# 초단기예보정보를 조회하기 위해 발표일자, 발표시각 예보지점 x좌표,
# 예보지점 y좌표의 조회 조건으로 자료구분코드, 예보값, 발표일자, 발표시각,
# 예보지점 x좌표, 예보지점 y좌표의 정보를 조회하는 기능

# api 키
serviceKey = 'zl6K9LBU80JqM4fFne5XAZQgvjZmLOVcL3%2B19Q8A4%2BuSLAoazArMi5mhcEM3UkB%2B%2FpUTmMzboOqVRLURsXay5g%3D%3D'
pageNo = '1' # 페이지번호
numOfRows = '10' # 한 페이지 결과 수
dataType = 'json' # 요청자료형식(xml/json) Default : xml
base_date = '20220813' #22년 8월 13일 발표
base_time='0630' #06시 30분 발표(30분 단위)
nx='55' # 예보지점 x좌표값
ny= '127' # 예보지점 y좌표값


# url ='	http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={}&pageNO={}&numOfRows={}&dataType={}&base_date{}&base_time={}&nx={}&ny={}'.format(serviceKey,pageNo, numOfRows,dataType, base_date,base_time,nx,ny)
url = "http://api.data.go.kr/openapi/tn_pubr_public_ovrspd_prvn_manage_api?serviceKey=zl6K9LBU80JqM4fFne5XAZQgvjZmLOVcL3+19Q8A4+uSLAoazArMi5mhcEM3UkB+/pUTmMzboOqVRLURsXay5g==&pageNo=1&numOfRows=1000&type=json"
response = requests.get(url,verify=False)
#dict_data = maltodict.parse(response.text)
#json_data = json.dumps(dict_data, ensure_ascii=False)

response = requests.get(url)
contents = response.text

## 보다 예쁘게 출력하기 위해..
##  indent는 들여쓴다는 의미
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

json_ob = json.loads(contents)
print(json_ob)
print(type(json_ob))

body = json_ob['response']['body']['items']
print(body)