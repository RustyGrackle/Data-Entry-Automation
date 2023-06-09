from bs4 import BeautifulSoup
import requests

#Constants
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.90711440039063%2C%22east%22%3A-121.95954359960938%2C%22south%22%3A37.57257324635536%2C%22north%22%3A37.97745533023803%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

# price = property-card-data

class Scraping:
    def __init__(self, url=ZILLOW_URL):
        self.website_html = requests.get(url, headers=headers).text
        self.soup = BeautifulSoup(self.website_html, "html.parser")
        self.all_houses = self.soup.select(selector=".property-card-link")
        self.all_links = self.listing_links()
        self.all_addresses = [a.text for a in self.all_houses]
        self.price = self.soup.select(selector=".srp__sc-16e8gqd-0")
        self.all_price = [a.get_text() for a in self.price]


    def listing_links(self):
        list=[]
        for a in self.all_houses:
            if "https" not in a.get("href"):
                list.append(f"https://www.zillow.com{a.get('href')}")
            else:
                list.append(a.get("href"))
        return list





