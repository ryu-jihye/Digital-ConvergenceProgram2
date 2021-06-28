#네이버 항공권
from selenium import webdriver
browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) #url로 이동

browser.find_element_by_link_text("가는날 선택").click()


#이번 달 29일, 30일 선택
#browser.find_elements_by_link_text("29")[0].click() #[0] -> 이번달
#browser.find_elements_by_link_text("30")[0].click()

#다음 달 29일, 30일 선택
#browser.find_elements_by_link_text("29")[1].click() #[0] -> 이번달
#browser.find_elements_by_link_text("30")[1].click()

#이번 달 27일, 다음 달 28일 선택
browser.find_elements_by_link_text("29")[0].click() #[0] -> 이번달
browser.find_elements_by_link_text("30")[1].click()


#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

#첫 번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)


#네이버 항공권 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) #url로 이동

browser.find_element_by_link_text("가는날 선택").click()


#이번 달 29일, 30일 선택
#browser.find_elements_by_link_text("29")[0].click() #[0] -> 이번달
#browser.find_elements_by_link_text("30")[0].click()

#다음 달 29일, 30일 선택
#browser.find_elements_by_link_text("29")[1].click() #[0] -> 이번달
#browser.find_elements_by_link_text("30")[1].click()

#이번 달 27일, 다음 달 28일 선택
browser.find_elements_by_link_text("29")[0].click() #[0] -> 이번달
browser.find_elements_by_link_text("30")[1].click()


#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색
browser.find_element_by_link_text("항공권 검색").click()
try:
#대기
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    #성공했을 때 동작 수행
    print(elem.text)#첫 번째 결과 출력
finally:
    browser.quit()

#첫 번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
