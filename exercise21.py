##################################
#
#  Exercise 21: Writing a file
#  https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
#
##################################

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(url)
response_html = response.text

soup = BeautifulSoup(response_html)

with open("./data/article.txt", "r+") as article:
    for line in soup.find_all("p")[6:]:
        article.write(line.getText())

        