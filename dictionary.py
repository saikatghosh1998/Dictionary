import sys
import requests
import re
from bs4 import BeautifulSoup as bs

url = "https://www.merriam-webster.com/dictionary/"

word = sys.argv[1]
url += word

r = requests.get(url)
soup = bs(r.content, 'lxml')

pos = soup.findAll("span", {"class": "fl"})[0].text
pronounce=soup.findAll("span",{"class":"pr"})[0].text
answer_list = soup.findAll("div", {"class": "vg"})[0]
meanings = answer_list.findAll("span",{"class":"dtText"})
#pos=meanings.findAll("a",{"class":"anchor"}).text
print("P.O.S" + ": "+pos)
print("pronounciation : "+pronounce)



#d=[]
for (i, meaning) in enumerate(meanings):
    print()
    
    print(str(i + 1) + ".", meaning.get_text(strip=True)) 
