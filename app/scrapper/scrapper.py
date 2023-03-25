import requests
from bs4 import BeautifulSoup
import random

def make_requests(url:str) -> dict:
    try:
        response = requests.get(url)
        print(response.status_code)
        return {"response": response}
    except:
        print("FAILED")
        return {"response": None}

def get_elements_page(url) -> None:
    response = make_requests(url)
    if response['response'] is not None:
        soup = BeautifulSoup(response['response'].content, 'html.parser')
        title = soup.find(id="firstHeading")
        print(title.string)

def get_all_link_page(url) -> None:
    response = make_requests(url)
    link_to_scrape = []
    if response['response'] is not None:
        soup = BeautifulSoup(response['response'].content, 'html.parser')
        all_links = soup.find(id="bodyContent").find_all("a")
        random.shuffle(all_links)
        for link in all_links:
            if link['href'].find("/wiki/") == -1:
                continue
            
            link_to_scrape.append("https://en.wikipedia.org"+link['href'])

    print(link_to_scrape)



if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    get_all_link_page(url)
    