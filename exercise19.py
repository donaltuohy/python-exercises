##################################
#
#  Exercise 19: Decode a webpage
#  https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
#
##################################

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(url)
response_html = response.text

soup = BeautifulSoup(response_html)

for line in soup.find_all("p")[6:]:
    print(line.text)