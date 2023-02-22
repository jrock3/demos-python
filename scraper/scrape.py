import urllib.request
import bs4
import csv

# scrape
url = 'https://news.ycombinator.com/'
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")
links = soup.select(".titleline > a")

# print to console
print(f"{len(links)} links found")

# save to file
with open('test_scrape.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter="\t")
    writer.writerow( ('Link', 'Title') )
    for link in links:
        writer.writerow( (link['href'], link.text) )