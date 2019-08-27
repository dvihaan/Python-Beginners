import numpy
import random
import urllib.request
from tkinter import *
from tkinter import ttk

class Game:
	
	def __init__(self, root):
		root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
		self.word = StringVar()
		self.guess = StringVar()
		self.lives = IntVar()
		self.result = StringVar()
		
		frame = Frame(root)
		frame.pack()
		#Label(frame, text='This is a test').grid(row=0, column=0)
		Label(frame, textvariable=self.word).grid(row=0, columnspan=2)
		Label(frame, text='Guess a letter:').grid(row=1, column=0)
		Entry(frame, textvariable=self.guess, width=1).grid(row=1, column=1)
		Label(frame, text='Lives left:').grid(row=2,column = 0)
		Label(frame, textvariable=self.lives).grid(row=2, column=1)
		Label(frame, textvariable=self.result).grid(row=3, columnspan=2)




def getWords():
    u = 'https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/'
    f = urllib.request.urlopen(u)
    contents = str(f.read()).split('\\n') 
    f.close()

    # 286 - 3283 <------ (lines that contain the words we need)
    wordList = []
    for w in range(286,3284):
        if len(contents[w]) > 15:
            wordList.append(contents[w][2:-6])
    return wordList
    
def game(word):
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print(word)
            print('You Win!!!')
            break
        if lives == 0:
            print('You got hung!...')
            print('the word was '+word)
            break
            
def wordPick():
    words = getWords()
    return random.choice(words)

def get_guess(word):
    printWord(word)
    print('Lives remaining: ' + str(lives))
    print('Incorrect Guesses: ' + str(wrongGuesses))
    guess = ''
    while True:
        guess = input('Guess a single letter: ')
        if len(guess) == 1:
            break
    return guess
    
def printWord(word):
    wordDisplay = ''
    for letter in word:
        if letterGuesses.find(letter) > -1:
            wordDisplay = wordDisplay + letter
        else:
            wordDisplay = wordDisplay + '-'
    print (wordDisplay)
    
def process_guess(guess, word):
    '''
    if your guess is one of the letters in the word, then change the
    blank space mapping to that letter in the dealer's word to the
    letter you guessed.
    
    if the letter you guessed is not one of the letters in the word,
    then one of your lives is removed and your remaining life count (global)
    is decreased by 1.
    '''
    global letterGuesses
    global lives
    global wrongGuesses
    
    if word.find(guess) < 0:
        lives = lives - 1
        wrongGuesses.append(guess)
        return False
    
    letterGuesses = letterGuesses + guess
    
    
    return gameEnd(word)
    
def gameEnd(word):
    '''
    if the length of the unique letters in the word is equal to
    the length of letterGuesses, then return True
    '''
    if len(letterGuesses) == len(set(word)):
        return True
    return False
    

'''
wrongGuesses = []
lives = 10
letterGuesses = ''
word = wordPick() 
game(word)
'''

root = Tk()
root.wm_title('Hangman')
game = Game(root)
root.mainloop()
