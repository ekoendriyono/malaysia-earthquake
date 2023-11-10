import requests
from bs4 import BeautifulSoup

def extraction():
    try:
        content = requests.get('https://www.detik.com/')
    except  Exception:
        return  None
    print(content.status_code)
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'box cb-mostpop'})
        # print(result.text)
        result = result.findChild('article')
        result = result.findChildren('a')
        print(result.text)
def show_data(result):
    if result is None:
        print('Empty Data')
        return
    return result