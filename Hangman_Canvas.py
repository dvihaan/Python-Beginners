from tkinter import *

class Hangman:

	def __init__(self, master):
		self.canvas = Canvas(master, width=255, height = 330)
		self.canvas.pack()
		h = int(self.canvas['height'])
		w = int(self.canvas['width'])
		self.cx = w/2
		self.cy = h/2
		
		self.drawFunctions = [
			lambda: self.canvas.create_line(self.cx+20,self.cy+220,self.cx+60,self.cy+120,width=5),
			lambda: self.canvas.create_line(self.cx+100,self.cy+220,self.cx+60,self.cy+120,width=5),
			lambda: self.canvas.create_line(self.cx+60,self.cy-110,self.cx+60,self.cy+120,width=5),
			lambda: self.canvas.create_line(self.cx+60,self.cy-110,self.cx-30,self.cy-110,width=5),
			lambda: self.canvas.create_line(self.cx-30,self.cy-60,self.cx-30,self.cy-110,width=5),
			lambda: self.canvas.create_oval(self.cx-60,self.cy-60,self.cx,self.cy,width=5),
			lambda: self.canvas.create_line(self.cx-30,self.cy,self.cx-30,self.cy+70,width=5),
			lambda: self.canvas.create_line(self.cx-30,self.cy+70,self.cx-50,self.cy+100,width=5),
			lambda: self.canvas.create_line(self.cx-30,self.cy+70,self.cx-10,self.cy+100,width=5),
			lambda: self.canvas.create_line(self.cx-60,self.cy+30,self.cx-30,self.cy+30,width=5),
			lambda: self.canvas.create_line(self.cx,self.cy+30,self.cx-30,self.cy+30,width=5),
			lambda: self.canvas.create_oval(self.cx-45,self.cy-40,self.cx-35,self.cy-30,fill='black'),
			lambda: self.canvas.create_oval(self.cx-15,self.cy-40,self.cx-25,self.cy-30,fill='black'),
			lambda: self.canvas.create_arc(self.cx-45,self.cy-25,self.cx-15,self.cy+5,start=0,extent=180,width=5),


		]
		
		#self.drawHangman()
		
		
	def drawHangman(self):	
		for f in self.drawFunctions:
			f()
'''
root = Tk()
test = Hangman(root)
root.mainloop()
'''
