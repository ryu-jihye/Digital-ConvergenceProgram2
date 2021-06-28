#이미지 링크
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=%EB%B8%94%EB%9E%99%20%EC%9C%84%EB%8F%84%EC%9A%B0&DA=MOR&rtmaxcoll=EM1&scckey=MV%7C%7C123215")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})

for image in images:
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url
        
    print(image_url)
 

#이미지 추출 2(여러 이미지 추출)
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=%EB%B8%94%EB%9E%99%20%EC%9C%84%EB%8F%84%EC%9A%B0&DA=MOR&rtmaxcoll=EM1&scckey=MV%7C%7C123215")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})

for idx, image in enumerate (images):
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url
        
    print(image_url)
    #requests를 통해 다시 접속
    image_res = requests.get(image_url)
    image_res.raise_for_status()
    
    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content) #movie1, movie2...
        

#1~5 이미지 추출
#이미지 추출 2
import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    images = soup.find_all("img", attrs={"class":"thumb_img"})
    
    for idx, image in enumerate (images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
            
        print(image_url)
        #requests를 통해 다시 접속
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content) #movie1, movie2...
            
        if idx >= 4: #상위 5개 이미지까지만 다운로드
            break