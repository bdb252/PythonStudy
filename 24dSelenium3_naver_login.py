# 셀레니움 모듈과 드라이버를 로드한다.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.naver.com/'
driver.get(url)

# XPATH를 이용해서 네이버 메인의 '로그인' 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/a/i').click()
# 로드와 상관없이 무조건 2초 대기
time.sleep(2)

# 로그인 페이지로 이동 후 아이디/비번의 입력상자를 찾은 후 정보입력
driver.find_element(By.NAME, 'id').send_keys('hanyilee')
time.sleep(2)
driver.find_element(By.NAME, 'pw').send_keys('1234')
time.sleep(2)

# 입력이 완료되면 '로그인'버튼 클릭해서 로그인 시도
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
# 셀레니움 로그인을 감지하므로 캡챠 화면이 뜬다.
time.sleep(30)
# 조금 긴 시간을 대기하면서 직접 입력

# 로그인이 완료되면 메인으로 자동 이동하므로 상단의 검색창에 검색어 입력
driver.find_element(By.NAME, 'query').send_keys('라이즈 원빈')
time.sleep(2)

# 검색을 눌러서 결과 확인
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(10)