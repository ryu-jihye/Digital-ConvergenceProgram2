#터미널에 pip install selenium
from selenium import webdriver

browser = webdriver.Chrome() #"./chromedriver_win32/chromedriver.exe"
browser.get("http://naver.com")

#터미널로 작업
#1 : python
#2 : from selenium import webdriver
#3 : browser = webdriver.Chrome()
#3-1 : browser.get("http://naver.com")
#4 : elem = browser.find_element_by_class_name("link_login")
#5 : elem
#6 : elem.click()
#7 : browser.back()
#8 : browser.forword()
#9 : browser.refresh()
#10 : broser.back()
#11 : elem = browser.find_element_by_id("query")
#12 : from selenium.webdriver.common,keys import Keys
#13 : elem.send_keys("나도 코딩")
#14 : elem.send_keys(Keys.ENTER)
#15 : elem = browser.find_element_by_tag_name("a")
#16 : for e in elem:
        #elem.get_attribute("href")
#17 : for e in elem:
        #e.get_attribute("href")
        
#다른 페이지로 이동
#browser.get("http://daum.net")
#elem = browser.find_element_by_name("q")
#elem.send_keys("나도코딩")
#elem.sned_keys(Keys.ENTER)
#elem.send_keys("나도코딩")

#elem = browser.find_element_by_name("q")
#elem.send_keys("나도코딩")
#elem = browser.find_element_by_xpath("//*[@id='daumSearch'])/fieldset/div/div/button[2]")
#elem.click()

#브라우저 종료
#browser.quit()
#exit()


