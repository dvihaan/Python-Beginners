import numpy
import random
import urllib.request
from tkinter import *
from tkinter import ttk

class Game:
	
	def __init__(self, root):
		root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
		self.word = ''
		
		self.letterGuesses = StringVar()
		self.guess = StringVar()
		self.guess.trace('w',self.limitEntry)
		self.lives = IntVar()
		self.result = StringVar()
		
		frame = Frame(root)
		frame.pack()
		Label(frame, textvariable=self.letterGuesses, font='Arial 24').grid(row=0, columnspan=2)
		Label(frame, text='Guess a letter:').grid(row=1, column=0)
		Entry(frame, textvariable=self.guess, width=1, font='Arial 16 bold').grid(row=1, column=1)
		Button(frame, text='Guess', command = self.process_guess).grid(row=2, columnspan=2)
		Label(frame, text='Lives left:').grid(row=3,column = 0)
		Label(frame, textvariable=self.lives).grid(row=3, column=1)
		Label(frame, textvariable=self.result).grid(row=4, columnspan=2)
		
		self.word = self.wordPick()
		self.printWord()
		self.lives.set(14)
		print(self.word)
	
	
	
	def limitEntry(self, *args):
		value = self.guess.get()
		if len(value)>1:
			self.guess.set(value[-1:])
			
		
	def getWords(self):
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
		
	def wordPick(self):
		self.wordList = self.getWords()
		return random.choice(self.wordList)
				
	def printWord(self):
		wordDisplay = ''
		letterGuesses = self.letterGuesses.get()
		for letter in self.word:
			if letterGuesses.find(letter) > -1:
				wordDisplay = wordDisplay + letter
			else:
				wordDisplay = wordDisplay + '-'
		self.letterGuesses.set(wordDisplay)
    				
	def process_guess(self):
		'''
		if your guess is one of the letters in the word, then change the
		blank space mapping to that letter in the dealer's word to the
		letter you guessed.
		
		if the letter you guessed is not one of the letters in the word,
		then one of your lives is removed and your remaining life count (global)
		is decreased by 1.
		'''
		guess = self.guess.get()		
		
		if self.word.find(guess) < 0:
			self.lives.set(self.lives.get() -1)
		else:
			self.letterGuesses.set(self.letterGuesses.get()+guess)
		self.printWord()
		

root = Tk()
root.wm_title('Hangman')
game = Game(root)
root.mainloop()
