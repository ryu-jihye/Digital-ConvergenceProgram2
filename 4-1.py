#광고 상품은 제외
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 제품은 제외합니다.> ")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text() #제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격
    rate = item.find("em", attrs={"class":"rating"}) #평점
    
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
            
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점 수
    
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점 없음"  
        
    print(name, price, rate, rate_cnt)   

#평점이 높은 것, 리뷰 수가 많은 것
#리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 제품은 제외합니다.> ")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text() #제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격
    rate = item.find("em", attrs={"class":"rating"}) #평점
    
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다.> ")
        continue
        
            
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점
    
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() #예 : (26)
        rate_cnt = rate_cnt[1:-1] #처음 ~ 맨 뒤쪽 바로 앞
        #print("리뷰 수", rate_cnt)
    else:
        print(" <평점 수 없는 상품 제외합니다.> ")
        continue
    
    if float(rate) >=  4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
    

#애플 상품은 제외
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 제품은 제외합니다.> ")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text() #제품명
    
    if "Apple" in name:
        print(" <Apple 상품 제외합니다> ")
        continue
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격
    rate = item.find("em", attrs={"class":"rating"}) #평점
    
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다.> ")
        continue
        
            
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점
    
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() #예 : (26)
        rate_cnt = rate_cnt[1:-1] #처음 ~ 맨 뒤쪽 바로 앞
        #print("리뷰 수", rate_cnt)
    else:
        print(" <평점 수 없는 상품 제외합니다.> ")
        continue
    
    if float(rate) >=  4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)