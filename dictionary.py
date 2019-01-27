import sys
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.merriam-webster.com/dictionary/"

try:
    word = sys.argv[1]
    url += word
except:
    print("Please Specify a Word !!")
    exit(-1)
    
try:
    r = requests.get(url)
    soup = bs(r.content, 'lxml')
except:
    print("Please check you internet connection !!")
    exit(-1)



try:
    pronounce=soup.findAll("span",{"class":"pr"})[0].text
except:
    pronounce="NA"
    
try:
    pos = soup.findAll("span", {"class": "fl"})[0].textpos = soup.findAll("span", {"class": "fl"})[0].text
    answer_list = soup.findAll("div", {"class": "vg"})[0]
    meanings = answer_list.findAll("span",{"class":"dtText"})
except:
    print("Word Not Found !!")
    exit(-1)


print()
print("P.O.S" + ": "+pos+"     |     "+"pronunciation: "+pronounce)

#d=[]
for (i, meaning) in enumerate(meanings):
    print()
    print(str(i + 1) + ".", meaning.text) 
