#!/usr/bin/python3

import random
import urllib.request
from tkinter import *
from tkinter import ttk
from Hangman_Canvas import Hangman

class Game:
	
	def __init__(self, root):
		#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
		self.wordList = self.getWords()
		self.word = ''
		
		self.letterGuesses = StringVar()
		self.guess = StringVar()
		self.guess.trace('w',self.limitEntry)
		self.lives = IntVar()
		self.result = StringVar()
		
		gameframe = Frame(root)
		gameframe.grid(row=0,column=0)
		self.canvasFrame = Frame(root)
		self.canvasFrame.grid(row=0,column=1)
		self.hangmanCanvas = Hangman(self.canvasFrame)
		canvas = Canvas(gameframe, width=340,height=440)
		Label(gameframe, textvariable=self.letterGuesses, font='Arial 24').grid(row=0, columnspan=2)
		Label(gameframe, text='Guess a letter:').grid(row=1, column=0)
		self.entry = Entry(gameframe, textvariable=self.guess, width=1, font='Arial 16 bold')
		self.entry.grid(row=1, column=1)
		self.guessButton = Button(gameframe, text='Guess', command = self.process_guess)
		self.guessButton.grid(row=2, columnspan=2)
		Label(gameframe, text='Lives left:').grid(row=3,column = 0)
		Label(gameframe, textvariable=self.lives).grid(row=3, column=1)
		Label(gameframe, textvariable=self.result).grid(row=4, columnspan=2)
		self.rButton = Button(gameframe, text='Play Again', command = self.restart)
		self.rButton.grid(row=5, columnspan=2)
		
		self.restart()
		
		
	def restart(self):
		self.letterGuesses.set('')
		self.word = random.choice(self.wordList)
		self.printWord()
		self.lives.set(14)
		self.entry.config(state='normal')
		self.guessButton.config(state='normal')
		self.guess.set('')
		self.result.set('')
		self.hangmanCanvas.canvas.delete(ALL)
		#print(self.word)
		
	def limitEntry(self, *args):
		value = self.guess.get()
		if len(value)>1:
			self.guess.set(value[-1:])			
		
	def getWords(self):
		u = 'https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/'
		f = urllib.request.urlopen(u)
		contents = str(f.read()).split('\\n') 
		f.close()
		wordList = []
		for w in range(286,3284):
			if len(contents[w]) > 14:
				wordList.append(contents[w][2:-6])
		return wordList
				
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
		guess = self.guess.get()				
		if self.word.find(guess) < 0:
			self.lives.set(self.lives.get() -1)
			self.hangmanCanvas.drawFunctions[13-self.lives.get()]()
		else:
			self.letterGuesses.set(self.letterGuesses.get()+guess)
		self.printWord()
		self.gameEnd()
		
	def gameEnd(self):
		if self.letterGuesses.get() == self.word:
			self.result.set('You Win!')
			self.entry.config(state='disabled')
			self.guessButton.config(state='disabled')
		if self.lives.get() == 0:
			self.result.set('You got hung!\n'+self.word)
			self.entry.config(state='disabled')
			self.guessButton.config(state='disabled')

root = Tk()
root.wm_title('Hangman')
game = Game(root)
root.mainloop()
