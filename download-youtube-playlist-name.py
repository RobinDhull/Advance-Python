import requests
from bs4 import BeautifulSoup

url = 'list-url' # Youtube PlayList url goes here

data = requests.get(url)
data = data.text
soup = BeautifulSoup(data, features="lxml")

playlist = soup.find_all("h4")
file = open('path/filename.txt',"w+")

for name in playlist:
    file.write(name.text)
file.close()