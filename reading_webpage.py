

import requests
from bs4 import BeautifulSoup
def read():
    url = 'https://www.google.com/search?q=weather%20near%20Yeswanthpur,%20Bengaluru&rlz=1C1CHBF_enIN992IN992&oq=ba&aqs=chrome.0.69i59j46i67i131i433i650j69i57j35i39j0i67i650j69i60l2j69i61.1086j0j7&sourceid=chrome&ie=UTF-8&llpgabe=CgovbS8wNWY4djk5&ved=2ahUKEwit-6m_4IX-AhVeSmwGHW9CC_YQ5pgEKAB6BAgFEAA'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().split('\n')[:1]

    result=''.join(text)
    result=result.replace('weather near Yeswanthpur, Bengaluru - Google SearchGoogle×Please click here if you are not redirected within a few seconds.    AllNewsShoppingBooks Images Maps Videos Search tools    Any timeAny timePast hourPast 24 hoursPast weekPast monthPast yearAll resultsAll resultsVerbatimDid you mean: weather near Yeshwanthpur, BangaloreYeswanthpur,','')
    return result

