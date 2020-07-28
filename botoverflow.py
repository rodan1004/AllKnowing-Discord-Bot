import requests
from bs4 import BeautifulSoup as Soup
import re

def stackoverflow(command):


    response = requests.get(f'https://stackoverflow.com/search?q={command}').text

    queries = Soup(response, 'lxml')
    all_questions = queries.find_all('a', class_='question-hyperlink', href=True)



    for question in all_questions:
        Q = question.text
        no_space_command = command.replace(' ', '')
        formatted_command = f'q:{no_space_command.lower()}'
        pattern = re.compile(formatted_command)
        no_space_Q = Q.replace(' ', '')
        formatted_Q = no_space_Q.lower()
        matches = pattern.finditer(formatted_Q)
        # # print(Q.replace(' ', ''))
        # if formatted_command == formatted_Q[3:]:
        #     print('yes')
        # else:
        #     print('no')

        # print(formatted_Q)
        # print(formatted_command)
        
        for match in matches:
            # if None:
            #     return 'Could not find this question on stackoverflow.'
            return f"https://stackoverflow.com{question['href']}"





