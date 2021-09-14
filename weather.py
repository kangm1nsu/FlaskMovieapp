import requests
from bs4 import BeautifulSoup

def callWeather():
    uri = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    response = requests.get(uri)
    doc_html = response.text
    soup = BeautifulSoup(doc_html,'html.parser') 
    target = soup.select_one(".info_temperature .todaytemp")
    temp = target.text
    dictTemp = {'temp' : temp}
    return dictTemp
