from urllib import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen("https://opensource.google/projects/explore/featured")
obj=bs(html.read())
print(obj.body.div.header.h1)
