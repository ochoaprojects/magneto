from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = input('please copy and paste your url: ')
print('')

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#finds the div
download = page_soup.find("div",{"class":"download"})

#finds the info hash
info_hash = download.a["href"]

print (info_hash)

print('')
input ("Press Enter to Exit")