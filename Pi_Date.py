from datetime import datetime
from datetime import timedelta

# 날짜 설정
now = datetime.now()                  
dt = now.date()                                                         # 오늘
tm = now.date() + timedelta(days=1)                                     # 내일
dat = now.date() + timedelta(days=2)                                    # 모래
today = dt.strftime("%Y년 %m월 %d일")                                    # 오늘 날짜를 문자열로 변경
tomorrow = tm.strftime("%Y년 %m월 %d일")                                 # 내일 날짜를 문자열로 변경
day_after_tomorrow = dat.strftime("%Y년 %m월 %d일")                      #모레 날짜를 문자열로 변경
