import random
from bs4 import BeautifulSoup
import requests
import numpy as np

words_list = ['view', 'advocate', 'discard', 'confess', 'disarray', 'assume', 'concrete', 'contrast', 'offensive',
              'buster', 'convey', 'compile', 'assert', 'appeal', 'pave', 'immersive', 'gadget', 'frame work',
              'firewall', 'embedded systems', 'consortium', 'authentication']

valid_urls = []
question = 'yes'

url = 'https://www.vocabulary.com/lists/'
rand_num_url = np.random.randint(0, 40000, 10)

for num in rand_num_url:
    num = str(num)
    randUrl = url + num
    html = requests.get(randUrl).content
    soup = BeautifulSoup(html, 'html.parser')

    not_found_result = soup.find('div', {'class': 'body-wrapper'}).find('div', {'class': 'page_notfound'})
    if not not_found_result:
        valid_urls.append(randUrl)

for link in valid_urls:
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('div', {'class': 'page_wordlist view-words'}).find('ol').find_all('li')
    for element in result:
        title = element.find('a').text
        if title not in words_list:
            words_list.append(title)

print(words_list, len(words_list))


HANGMAN = (
    """
 ------
|     |
|
|
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|     +
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|    -+
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|    -+-
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|   /-+-
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|   /-+-/
|
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|   /-+-/
|     |
|
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|
|
----------
"""
    ,
    """
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    |
|    |
----------
"""
    ,
    """
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    | |
|    | |
----------
"""
)


class HangmanGame:
    def _init_(self):
        # self.choice = None
        self.word = random.choice(words_list)
        self.blanks = ''
        self.chosen_letters = []

    def choose_letter(self):
        choice = '10'
        while not choice.isalpha() or len(choice) > 1:
            choice = input("Choose a letter: ")
        return choice

    def letter_detection(self, choice, failed_score):
        self.blanks = ''
        word = self.word
        choice = choice.lower()
        if choice not in word:
            failed_score += 1
        self.chosen_letters.append(choice)
        for letter in word:
            if letter != ' ':
                if letter in self.chosen_letters:
                    self.blanks += letter
                else:
                    self.blanks += '_'
            else:
                self.blanks += ' '

        return self.blanks, failed_score

    def shape(self, failed_score):
        shape_of_hangman = HANGMAN[failed_score]
        return shape_of_hangman

    def main(self):
        global question
        while question.lower() == 'yes':
            chosen_letter = []
            first_blanks = ''
            failed_score = 0
            for letter in self.word:
                if letter != ' ':
                    first_blanks += '_'
                else:
                    first_blanks += ' '
            print(first_blanks)
            while self.blanks != self.word:
                print(self.shape(failed_score))
                if failed_score == 10:
                    self.blanks = self.word
                    break
                choice = self.choose_letter()
                chosen_letter.append(choice)
                print(f'chosen letters: {chosen_letter}')
                print(self.letter_detection(choice, failed_score)[0])
                failed_score = self.letter_detection(choice, failed_score)[1]

            if failed_score == 10:
                print('YOU LOSE THE GAME:(')
            else:
                print('YOU WIN!!!')

            question = input('Want to play again?')
            self.word = random.choice(words_list)
            self.blanks = ''
            self.chosen_letters = []

        print('Okay, have a nice day!')


game = HangmanGame()
game.main()