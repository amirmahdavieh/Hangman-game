# Hangman Game with Vocabulary Words

Welcome to the Hangman Game with a twist! This Python script allows you to play the classic Hangman game using a randomly selected vocabulary word. The words are fetched dynamically from vocabulary.com, making each game a unique language challenge. The project was completed in 2020.

## Prerequisites

Make sure you have the following dependencies installed:

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): `pip install beautifulsoup4`
- [NumPy](https://numpy.org/): `pip install numpy`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/amirmahdavieh/Hangman-game.git
   ```

2. Run the script:

   ```bash
   python hangman_game.py
   ```

3. Follow the on-screen instructions to guess the letters and complete the word. You have up to 10 attempts before the Hangman is complete.

4. After each game, you'll have the option to play again.

## How it Works

1. The script fetches a random list of words from vocabulary.com.
2. The Hangman game initializes with a randomly selected word from the list.
3. The player is prompted to guess letters until the word is complete or the Hangman is fully drawn.
4. The game provides feedback on the chosen letters and updates the Hangman figure accordingly.
5. After each game, the player can choose to play again.

## Customization

Feel free to customize the script or integrate it into your projects. You can modify the list of words or enhance the game's functionality to suit your preferences.

## Acknowledgments

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping functionality.
- [NumPy](https://numpy.org/) for numerical operations in Python.
- Hangman ASCII art sourced from an open repository.

Have fun playing Hangman and expanding your vocabulary!
