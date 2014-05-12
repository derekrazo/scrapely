"""

This example scrapes from the wiki article for Fish, 
trains on the title, and returns gill.

Feel free to gasp at the raw power at you fingertips 
in only... is that like 10 lines of JS? Damn. 

"""

from scrapely import Scraper
s = Scraper()

url1 = 'https://en.wikipedia.org/wiki/Fish'
data = {'title': 'Fish'}
s.train(url1, data)

url2 = 'https://en.wikipedia.org/wiki/Gill'
print(s.scrape(url2))


