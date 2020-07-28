import requests
from bs4 import BeautifulSoup as Soup

def internet_joke_api():

    internet_joke = requests.get('https://geek-jokes.sameerkumar.website/api').text

    return internet_joke

# print(internet_joke)

# joke = Soup(response, 'lxml')

# main_joke = joke.find('div', class_='jsonPrimitiveValue')

# print(main_joke.span) 