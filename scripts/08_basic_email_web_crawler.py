from bs4 import BeautifulSoup
import requests

url = input('Enter a URL (include `http://`): ')
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")

print(html)

list = []
for i in soup.find_all("a",href=True):
    list.append(i)
    print("leiitud links: ", i)

