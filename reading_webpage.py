

import requests
from bs4 import BeautifulSoup
def read():
    url = 'ENTER THE URL OF GOOGLE INTERFACE WEATHER FORCASTING'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().split('\n')[:1]

    result=''.join(text)
    
    return result

