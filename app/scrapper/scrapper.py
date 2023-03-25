import requests
from bs4 import BeautifulSoup

def make_requests(url:str)->dict:
    try:
        response = requests.get(url,)
        print(response.status_code)
        return {"response": response}
    except:
        print("FAILED")
        return {"response": None}

def get_elements_page() -> None:
    response = make_requests("https://en.wikipedia.org/wiki/Web_scraping")
    if response['response'] is not None:
        soup = BeautifulSoup(response['response'].content, 'html.parser')
        title = soup.find(id="firstHeading")
        print(title.string)



if __name__ == "__main__":
    get_elements_page()