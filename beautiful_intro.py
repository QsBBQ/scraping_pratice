from bs4 import BeautifulSoup  # BeautifulSoup4 package
from urllib2 import urlopen
import os

my_address = "https://docs.python.org/2/whatsnew/2.7.html"
html_page = urlopen(my_address)
html_text = html_page.read()
# soup = BeautifulSoup(html_text, "lxml")  # second param tells bs which parser to use
#
# # print(soup.get_text().encode("utf-8"))
# result  = soup.get_text().encode("utf-8")
# text = os.linesep.join([s for s in result.splitlines() if s])
# print(text)

# Another example with html parser
soup = BeautifulSoup(html_text, "html.parser")  # second param tells bs which parser to use
# scrape all images
images= []
images= soup.find_all("img")
for img in images:
  print img['src']
