# Hangman game
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in lettersGuessed:
        if char in secretWord:
            secretWord = secretWord.replace(char, '')
    return len(secretWord) == 0


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for char in secretWord:
        if char in lettersGuessed:
            result += char
        else:
            result += '_ '
    return result;



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLetters = string.ascii_lowercase
    result = ''
    for char in allLetters:
        if char not in lettersGuessed:
            result += char
    return result


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    numOfGuesses = 8
    lettersGuessed = ''

    while numOfGuesses > 0:
        print('You have ' + str(numOfGuesses)+ ' guesses left.')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ')

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            if guess in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                numOfGuesses -= 1
        print('-'*15)
        print('')

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break

    print('Sorry, you ran out of guesses. The word was ' + secretWord)
    print('')


#helper
def check():
    global numOfGuesses
    global totalGuesses
    global top_label
    global secretWord
    global lettersGuessed
    global avals
    global progress

    char = guess.get()

    if numOfGuesses == totalGuesses:
        top_label['text'] = 'GAMEOVER'

    elif char in lettersGuessed:
        top_label['text'] = f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}"

    else:
        numOfGuesses += 1
        lettersGuessed += char
        aval_chars['text'] = f"Avaliable letters: {avals.replace(char, '')}"
        progress['text'] = f"letter guessed: '{lettersGuessed}' and {totalGuesses-numOfGuesses} guesses remaining"
        guess.delete(0,5)

        if char in secretWord:
            top_label['text'] = f'Good guess: {getGuessedWord(secretWord, lettersGuessed)}'
        else:
            top_label['text'] = f'Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}'

        if isWordGuessed(secretWord, lettersGuessed):
            top_label['text'] = 'The secret word is {secretWord}. Congratulations, you won!'

    return

def reset():
    global wordlist
    global numOfGuesses
    global totalGuesses
    global top_label
    global secretWord
    global lettersGuessed
    global avals
    global aval_chars
    global progress

    avals, numOfGuesses = string.ascii_lowercase, 0
    secretWord = chooseWord(wordlist)
    lettersGuessed = ''
    top_label['text'] = f'I am thinking of a word that is {str(len(secretWord))} letters long.'
    aval_chars['text'] = f'Avaliable letters: {avals}'
    progress['text'] = f"letter guessed: '{lettersGuessed}' and {totalGuesses} guesses remaining"

    return

if __name__ == "__main__":

    numOfGuesses, totalGuesses, lettersGuessed = 0, 8, ''

    import tkinter

    #create window
    root = tkinter.Tk()
    root.title("Welcome to game, hangman!")
    root.geometry("500x150")

    #start game
    wordlist = loadWords()
    secretWord = chooseWord(wordlist)

    #first output
    top_label = tkinter.Label(root, text=f'I am thinking of a word that is {str(len(secretWord))} letters long.')
    top_label.grid(row=1, column=1)

    #available letters
    avals = string.ascii_lowercase
    aval_chars = tkinter.Label(root, text=f'Avaliable letters: {avals}')
    aval_chars.grid(row=2, column=1)

    #progress
    progress = tkinter.Label(root, text=f"Letters guessed: '{lettersGuessed}' and {totalGuesses-numOfGuesses} guesses remaining")
    progress.grid(row=3, column=1)

    #entry
    guess = tkinter.Entry(root, width=3)
    guess.grid(row=4, column=1)

    #btn
    check = tkinter.Button(root, text="check", command=check)
    check.grid(row=4, column=0)
    reset = tkinter.Button(root, text="reset", command=reset)
    reset.grid(row=4, column=2)


    root.mainloop()
    root.destroy()


    # # Load the list of words into the variable wordlist
    # # so that it can be accessed from anywhere in the program
    # wordlist = loadWords()
    #
    # #choose a random secret word
    # secretWord = chooseWord(wordlist)
    #
    # #start the hangman game
    # hangman(secretWord)
