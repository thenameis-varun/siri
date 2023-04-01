# import pywhatkit

# # Prompt the user to enter the location
# location = input("Enter your location: ")

# # Construct the search query
# query = f"{location} weather"

# # Search for the weather using Google
# pywhatkit.search(query)
# import pyowm

# # Prompt the user to enter the location
# location = input("Enter your location: ")

# # Set up the OpenWeatherMap API key
# owm = pyowm.OWM('AIzaSyCpSE7LYHw34oo41xu7KO5C5eS0TN_fzzQ')  # Replace YOUR-API-KEY with your actual API key

# # Get the current weather observation for the location
# observation = owm.weather_at_place(location)
# weather = observation.get_weather()

# # Get the weather status and print it out
# status = weather.get_status()
# print("The weather in", location, "is", status)

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

