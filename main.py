from bs4 import BeautifulSoup
import urllib
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}
pages_data = [0]


def get_pages(pages):
    pages_str = pages+"0"
    pages_int = int(pages_str)
    for i in range(1, pages_int):
        if i % 10 == 0:
            pages_data.append(i)


def get_dork(dork):
    print("\n")
    for i in pages_data:
        dork_page = str(i)
        dork_url = "https://www.google.com/search?q=" + \
            dork + "&start=" + dork_page
        dork_req = requests.get(dork_url, headers=headers).text
        dork_soup = BeautifulSoup(dork_req, "html.parser")
        for j in dork_soup.find_all('div', attrs={'class': 'g'}):
            get_link = j.find('a', href=True)
            get_link_href = get_link['href']
            print("[+]" + get_link_href)

dork = input("Input Data : ")
pages = input("Input Pages : ")


get_dork(dork)
get_pages(pages)
