import requests
from bs4 import BeautifulSoup as Soup
import re

def stackoverflow(command):

    # a request to load the stackoverflow command link
    response = requests.get(f'https://stackoverflow.com/search?q={command}').text
    
    #getting all the a html element tag with the class of question-hyperlink
    queries = Soup(response, 'lxml')
    all_questions = queries.find_all('a', class_='question-hyperlink', href=True)


    #looping and through all the result and finding all of questions that maches the question from the command parameter of the stackoverflow function.
    for question in all_questions:
        Q = question.text
        no_space_command = command.replace(' ', '')
        formatted_command = f'q:{no_space_command.lower()}'
        pattern = re.compile(formatted_command)
        no_space_Q = Q.replace(' ', '')
        formatted_Q = no_space_Q.lower()
        matches = pattern.finditer(formatted_Q)
        
        #this returns the link of the questions that are a match to the question given to the command parameter of the stackoverflow function.
        for match in matches:
            return f"https://stackoverflow.com{question['href']}"





