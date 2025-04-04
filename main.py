from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키입력
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select #select 접근
from selenium.webdriver.support.ui import WebDriverWait #로딩 확인
from selenium.webdriver.support import expected_conditions as EC
import time

# name = input('이름을 입력 하세요.\n')
# birth_day = input('생년월일을 입력 하세요.\n')
# print(name, birth_day)
# print(name+birth_day)


url = "https://www.unsin.co.kr/unse/free/todayline/form?linenum=01&sid=tunse"

driver = webdriver.Chrome()
driver.get(url)
WebDriverWait(driver,1).until(lambda d: d.execute_script("return document.readyState") == "complete")

# element 선택
el_user = driver.find_element(By.ID, 'user_name')
el_sex = Select(driver.find_element(By.ID, 'sex'))
el_yy = Select(driver.find_element(By.ID, 'birth_yyyy'))
el_mm = Select(driver.find_element(By.ID, 'birth_mm'))
el_dd = Select(driver.find_element(By.ID, 'birth_dd'))
el_hh = Select(driver.find_element(By.ID, 'birth_hh'))
el_sol = Select(driver.find_element(By.ID, 'birth_solunar'))
el_btn = driver.find_element(By.ID, 'btnOk')

# 값 입력
el_user.send_keys('')
el_sex.select_by_value('')
el_yy.select_by_value('')
el_mm.select_by_value('')
el_dd.select_by_value('')
el_hh.select_by_value('')
el_sol.select_by_value('')

# btn 클릭
el_btn.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"viewer_icon_Box")))
el_header = driver.find_element(By.XPATH, '//*[@id="viewerBox"]/div/div/div[1]/div[2]/div/h3').text
el_boxs = driver.find_elements(By.CLASS_NAME, 'bg-box')

content = {}
for box in el_boxs:
    el_h2 = box.find_elements(By.TAG_NAME, 'h2')
    el_p = box.find_elements(By.TAG_NAME, 'p')
    if el_h2:
        content[el_h2[0].text] = el_p[0].text
    else:
        content[el_header] = el_p[0].text

for key, value in content.items():
    print(f"키: {key}, 값: {value}\n")

driver.close()