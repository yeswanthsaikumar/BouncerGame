from tkinter import *
from PIL import Image , ImageTk
import sys
from tkinter import messagebox
import random
import time

root = Tk()
root.title('BOUNCER')
root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(Image.open('im.jpeg')))
root.resizable(0,0)
#GIF = ImageTk.PhotoImage(Image.open('ph.gif')
root.wm_attributes('-topmost',1)
canvas=Canvas(root,width=600,height=600,bd=0,highlightthickness=0,bg='purple')
canvas.pack()
root.update()
#variable for no of hits
ms = messagebox.askquestion("DIALOGUE BOX","DO YOU WANT TO START GAME")
if ms == 'yes':	
	count = 239487
	player = ''

	class Ball:
		def __init__(self,canvas,color,paddle):
			random.seed()
			self.canvas = canvas
			self.color = color
			self.id = self.canvas.create_oval(0,0,25,25,fill=color)
			#self.canvas.move(self.id,250,400)
			self.paddle = paddle
			#start = [23,234,5,1,89,48,68,67]
			self.x = 40#random.randrange(0,601)
			self.y = 30#random.randrange(0,400)
			#self.canvas_height = self.canvas.winfo_heigth()
	
		def hit_paddle(self,pos):
			paddle_pos = self.canvas.coords(self.paddle.id)
			if pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0]:
				if pos[3] <=paddle_pos[3] and pos[3] >= paddle_pos[1]:
					return True
				return False

		def ball_misses(self,pos):
			paddle_pos = self.canvas.coords(self.paddle.id)
			if pos[1] > paddle_pos[3]:
                		return True
			return False

		def draw(self):
			pos = self.canvas.coords(self.id)
			if pos[1] <= 0:
				self.y = 3
			elif pos[3] >= 600:#self.canvas_height:
				self.y = -3
			if self.hit_paddle(pos):		
				self.y = -3
				global count
				count += 1 
			if pos[0] <= 0:
				self.x = 3
			elif pos[2] >= 600:
				self.x= -3 
			#ball crosses the paddel
			if self.ball_misses(pos) :
				messagebox.showinfo("GAME OVER","YOUR SCORE IS " + str(count))
				sys.exit()
			self.canvas.move(self.id,self.x,self.y)
		

	class Paddle:
		def __init__(self,canvas,color):
			self.canvas = canvas
			self.color = color
			self.id= self.canvas.create_rectangle(300,500,400,510,fill=color)
			self.canvas.move(self.id,0,0)
			self.pos = self.canvas.coords(self.id)
			self.x = 0
			self.y = 0
			self.canvas.bind_all('<KeyPress-Left>',self.left_click)
			self.canvas.bind_all('<KeyPress-Right>',self.right_click)
		def draw(self):
			pos = self.canvas.coords(self.id)
			if pos[0] <= 0:
				self.x = 3
			elif pos[2] >= 600:
				self.x = -3
			self.canvas.move(self.id,self.x,self.y)
			#pass
		def left_click(self,event):
			self.x = -5
			#pass
		def right_click(self,event):
			self.x = 5
			#pass
	paddle = Paddle(canvas,'orange')
	ball = Ball(canvas,'white',paddle)

	while 1:
		paddle.draw()
		ball.draw()
		root.update_idletasks()
		root.update()
		time.sleep(0.01)

	root.mainloop()
