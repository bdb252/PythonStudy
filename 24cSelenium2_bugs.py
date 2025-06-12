from selenium import webdriver
driver = webdriver.Chrome() 

# driver.implicitly_wait(5)

import time
# time.sleep

url = 'https://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

time.sleep(5)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser') 

song_data = []
songs = soup.select('#CHARTrealtime > table > tbody > tr')
for song in songs:
  # 순위
  rank = song.select('td:nth-child(4) > div > strong')[0].text
  # 노래제목
  title = song.select('th > p > a')[0].text
  # 가수
  singer = song.select('td:nth-child(8) > p > a')[0].text
  # 앨범명
  album = song.select('td:nth-child(9) > a')[0].text
  
  # 크롤링한 내용을 콘솔에 출력
  print(rank, title, singer, album, sep="|")
  # 파싱한 정보를 리스트에 추가
  song_data.append(['Bugs', rank, title, singer, album])
  
# 판다스 모듈 임포트
import pandas as pd
# 데이터프레임으로 변환시 상단에 컬럼명을 추가
columns = ['서비스', '순위', '타이틀', '가수', '앨범명']  
pd_data = pd.DataFrame(song_data, columns=columns)
# 데이터프레임 상위 5개 행을 출력해서 확인
print(pd_data.head())
# 엑셀로 저장
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)


# 순위
#CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > strong
# 노래제목
#CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a
# 가수 
#CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(8) > p > a
# 앨범명
#CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(9) > a