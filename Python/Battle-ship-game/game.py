# ############## Naval Battle-Ship GUI game #################### #
from tkinter import *
from tkinter import messagebox
import pygame
import random
import os
from tkinter import ttk
import PIL
from PIL import Image , ImageTk
# ################# ###################### ##################### #


class Create:
	player_health , computer_health = 0 , 0
	def __init__(self , root ,row , col , txt , bg , fg ,num , parent):
		self.root , self.row , self.col, self.txt ,self.bg , self.fg ,self.num , self.parent  = root , row , col , txt , bg , fg ,num  , parent
		self.button = Button(self.root , text = self.txt , bg = self.bg , fg = self.fg  ,  height = 1, width = 3 , font = ('Courier' ,15) , command  = self.change )
		self.button.grid(row= row ,  column = col)

	def intelligence():
		intel = [ i.give_id for i in Main.lis_player if i.get_bg == 'Red']
		return intel

	@staticmethod
	def hint():
		if Main.flag == True:
			hin = [ i.give_id for i in Main.lis_comp if i.get_fg == 'Red']
			hin = (random.choice(hin)-64) + random.randint(0 , 3)
			messagebox.showinfo('Compass' , f'One of Enemy Ship is at box location { hin }')
		else: messagebox.showinfo('Message' , 'Kindly place yours ships first !!')
	
	@property
	def get_bg(self):
		return self.bg
	@property	
	def get_fg(self):
		return self.fg
	@property	
	def give_id(self):
		return self.num

	def place_enemy(self):
		self.button.configure(fg = 'Red')
		self.fg = 'Red'		

	def change(self):	
		if Main.flag == False:
			if self.num < 65:
				if self.bg == 'White':
					self.button.configure(bg = 'RED')
					self.bg = 'Red'
					return False
		if Main.flag == True:
			if self.num < 65: return None
		if Main.flag == True: # ################ FIRING MODE ############### #
			z = Create.intelligence()
			a = random.choice(z) + random.randint( 0 , Intro.diff_level )		

# ################# FIRING ON COMPUTER REGION #######################
			if self.fg == 'Red' and self.num > 64:
				self.button.configure(bg = 'BLUE' )
				self.bg = 'Blue'
				play(exp_sound)
				Create.computer_health-=1

				Main.player_health['text'] = f'Your-Health : {Create.player_health}'
				Main.computer_health['text'] = f'Comp-Health : {Create.computer_health}'

				if Create.computer_health == 0:
					m=messagebox.askquestion('HURRAH ! ' , 'YOU SANK Enemie\'s ARMADA ! '+'\n'+'Do you want to play again ?')
					if m == 'yes': Main.destroy_comp(self.parent , flag = False)
					if m == 'no': exit()		
					return False
			
			if self.fg == 'Yellow' and self.num > 64:
				self.button.configure(bg = 'pink')
				self.bg = 'pink'

				pres = 0
				for i in Main.lis_comp:
					if self.num - i.num == -1 or self.num - i.num == 1:
						if i.fg=='Red':
							pres+=1
					if i.num - self.num == -8 or i.num  - self.num == 8:
						if i.fg == 'Red':
							pres+=1
					if i.num - self.num == -7 or i.num - self.num == 7:
						if i.fg == 'Red':
							pres+=1
					if i.num -self.num == - 9 or i.num -self.num == 9:
						if i.fg == 'Red':
							pres+=1

				self.button['text'] = str(pres)
				play(shot_sound)

# ################## FIRING ON PLAYER REGION #########################
			
			for k in Main.lis_player:
				if k.give_id == a:
					if k.bg == 'Red' :
						k.button.configure(bg = 'BLUE' )
						k.bg = 'Blue'
						play(exp_sound)
						Create.player_health-=1
						
						Main.player_health['text'] = f'Your-Health : {Create.player_health}'
						Main.computer_health['text'] = f'Comp-Health : {Create.computer_health}'

						if Create.player_health == 0:
							m = messagebox.askquestion('OPSS' , '...You Lost... Enemy Sunk your fleet'+'\n'+'Do You want to play again ?')
							if m == 'yes': Main.destroy_comp(self.parent , flag = False)
							if m == 'no': exit()	
							return False

					if k.bg == 'White' :
						k.button.configure(bg = 'pink')
						k.bg = 'pink'
						play(shot_sound)
					break
		Main.player_health['text'] = f'Your-Health : {Create.player_health}'
		Main.computer_health['text'] = f'Comp-Health : {Create.computer_health}'
	
	def __repr__(self):
		return f'----Intro of Class----\nThis class holds functions for buttons\nWhich makes grids for enemy and player and\nholds logic for all buttons\n----Doc---\n{ Create.__dic__ }'				

class Main:
	flag = False
	lis_player , lis_comp = [] , []
	def __init__(self):
		self.app = Tk()
		self.app.geometry('900x500'+'+170+100') , self.app.resizable(0,0) , self.app.title('Battle Ship Game')
		self.photo = ImageTk.PhotoImage(Image.open('header.jpg').resize( (900,500) ))
		Label(self.app ,image = self.photo ).pack()

		Label(self.app , text = '< NAVAL-BATTLE-GAME >',relief='groove', bg = 'Black',  fg = 'gold' , font = ('veredana italic' ,15 , 'bold') ).place(x = 330 , y = 0)
		Label(self.app , text = 'Your-Region',relief='groove', bg = 'white',  fg = 'red' , font = ('veredana italic' , 12, 'bold' ) ).place(x = 110 , y = 30)
		
		self.frame_left =  Frame(self.app)
		self.frame_left.place(x = 0 , y = 60)

		Label(self.app , text = 'Enemy\'s Region',relief='groove'  , bg = 'white',  fg = 'red' , font = ('veredana italic' , 12,'bold' ) ).place(x = 680 , y = 30)

		self.frame_right = Frame(self.app)
		self.frame_right.place(x = 535 , y = 60 )

		show_grid(self.frame_left , parent = self)
		show_grid(self.frame_right,  self , True )

		strt_bttle = Button(self.app , height = 3 , text = 'START BATTLE',relief='groove' , bg = 'gold',width = 15 , fg = 'black' , font = ('veredana italic' , 13,  'bold' ) , command =  start_place )
		strt_bttle.place(x = 371 , y = 140)
		Main.player_health = Label(self.app , text = f'Your-Health : {Create.player_health}',relief='groove'  , bg = 'white' , fg = 'purple' , font = ('veredana italic' , 14,'bold' ) )
		Main.computer_health = Label(self.app , text = f'Comp-Health : {Create.computer_health}', relief='groove', bg = 'white' , fg = 'purple' , font = ('veredana italic' , 14,'bold' ) )

		Main.player_health.place(x = 10 , y = 380) , Main.computer_health.place(x = 730 , y = 380)

		self.time_count = Label(self.app ,relief='groove' ,  bg = 'white' , fg = 'Blue' , font = ('veredana italic' , 14 , 'bold' ) )
		self.time_count.place(x = 380 , y = 280)

		new_gme = Button(self.app , text = 'NEW GAME' , width=20 , bg = 'seagreen3' , fg = 'black' , font = ('veredana' , 12 , 'bold' ),  command = lambda : Main.destroy_comp(self))
		compas = Button(self.app , text = 'Compas', width=20 , bg = 'Yellow' , fg = 'black' , font = ('veredana' , 12 , 'bold' ),  command = Create.hint)
		back_gme = Button(self.app , text = 'Back' , bg = 'Yellow' , fg = 'black', width = 10 , font = ('veredana' , 12 , 'bold' ),  command = self.back )
		new_gme.place(x = 340 , y = 400), compas.place(x = 340 , y = 450), back_gme.place(x = 10 , y = 450)

		new_gme.bind('<Enter>' , lambda event, bt_this = new_gme : on_enter(event ,  bt_this ) ) 
		new_gme.bind('<Leave>' ,  lambda event, bt_this = new_gme : on_leave( event , bt_this ) ) 		
		compas.bind('<Enter>' , lambda event, bt_this = compas  : on_enter(event ,  bt_this ) ) 
		compas.bind('<Leave>' ,  lambda event, bt_this = compas , bg_color = 'yellow' : on_leave( event , bt_this , bg_color ) ) 		
		back_gme.bind('<Enter>' , lambda event, bt_this = back_gme  : on_enter(event ,  bt_this ) ) 
		back_gme.bind('<Leave>' ,  lambda event, bt_this = back_gme , bg_color = 'yellow' : on_leave( event , bt_this , bg_color ) ) 		
		strt_bttle.bind('<Enter>' , lambda event, bt_this = strt_bttle  : on_enter(event ,  bt_this ) ) 
		strt_bttle.bind('<Leave>' ,  lambda event, bt_this = strt_bttle , bg_clr = 'gold'  : on_leave( event , bt_this , bg_clr ) ) 		


		self.dis()
		self.app.mainloop()
	def dis(self):
	    global sec , minu , curr_tim , flag
	    self.job = self.app.after(1000 , self.dis)
	    sec+=1
	    if sec >= 60:
	        sec = 0
	        minu+=1
	    curr_tim = f'{minu}m : {sec}s'
	    self.time_count['text'] = f'Time-Elapsed\n\n{curr_tim}'

	def cancel(self ):
		    if self.job is not None:
		        self.app.after_cancel(self.job)
		        self.job = None

	@staticmethod
	def destroy_comp(self , flag = True):
		self.cancel() 
		self.app.destroy()
		global sec , minu
		Main.flag , sec , minu = False, 0 , 0
		Create.player_health , Create.computer_health , Main.lis_comp , Main.lis_player = 0 , 0 , [] , []
		Main()

	def back(self):
		'Initializing every thing and destroying current window'
		self.cancel()
		self.app.destroy()
		global sec , minu
		Main.flag , sec , minu = False, 0 , 0
		Create.player_health , Create.computer_health , Main.lis_comp , Main.lis_player = 0 , 0 , [] , []
		Intro()

	def __repr__(self):
		return f'----Intro of Class----\nThis class holds GUI for Game\nIt has frames that have grids for enemy and player\nIt holds button having different functions\n----Doc---\n{ Main.__dic__ }'				


class Intro(Main):
	diff_level , dic = 10 , { 10  : '--Easy--', 7 : '--Hard--' , 4 : ' --Insane--' }
	inverted_dic = { value:key for (key,value) in dic.items() }
	
	def __init__(self):
		self.root = Tk()
		self.root.geometry('500x500'+'+300+100') , self.root.resizable(0,0) , self.root.title('Welcome Battle-ship')
		self.photo = ImageTk.PhotoImage(Image.open('image.jpg').resize( (500,500) ))
		Label(self.root ,image = self.photo ).pack()
		self.new_srt = Button(self.root , text = 'Play Game',relief=SUNKEN ,width = 20, bg = 'seagreen3' , fg = 'black' , font = ('veredana' , 15 , 'bold' ),  command = self.play  )
		self.new_srt.place(x = 140 , y = 200)
		self.instr = Button(self.root , text = 'Instructions',relief=SUNKEN ,width = 20, bg = 'seagreen3' , fg = 'black' , font = ('veredana' , 15 , 'bold' ),  command = self.instructions  )
		self.instr.place(x = 140 , y = 300)
		self.diff_lev = Button(self.root , text = 'Difficulty',relief=SUNKEN ,width = 20, bg = 'seagreen3' , fg = 'black' , font = ('veredana' , 15 , 'bold' ),  command = self.level_difficulty  )
		self.diff_lev.place(x = 140 , y = 400)

		self.new_srt.bind('<Enter>' , lambda event, bt_this = self.new_srt : on_enter(event ,  bt_this ) ) 
		self.new_srt.bind('<Leave>' ,  lambda event, bt_this = self.new_srt : on_leave( event , bt_this ) ) 		
		self.instr.bind('<Enter>' , lambda event, bt_this = self.instr : on_enter(event ,  bt_this ) ) 
		self.instr.bind('<Leave>' ,  lambda event, bt_this = self.instr : on_leave( event , bt_this ) ) 		
		self.diff_lev.bind('<Enter>' , lambda event, bt_this = self.diff_lev : on_enter(event ,  bt_this ) ) 
		self.diff_lev.bind('<Leave>' ,  lambda event, bt_this = self.diff_lev : on_leave( event , bt_this ) ) 		


		self.root.mainloop()

	def play(self):
		self.root.destroy()
		super().__init__()

	def instructions(self):
		self.new_root = Toplevel(self.root)
		self.new_root.geometry('600x380') , self.new_root.title('Instructions') , self.new_root.resizable(0,0)
		Label(self.new_root , text = 'INSTRUCTIONS',relief='groove' , bg = 'Black' , fg = 'Gold'  , font = ('helvitca' , 12 , 'bold')).pack() , Label(self.new_root).pack()
		Lb1 = Listbox( self.new_root,height = 20 , width = 80 , font = ('helvitca' , 10 , 'bold') )
		with open('Instructions.txt' ,'r') as f:
			for i in f.readlines():
				Lb1.insert(END, i )
		Lb1.pack(pady = 10 , padx = 5)
	
	def level_difficulty(self):
		self.diff_wind = Toplevel()
		self.diff_wind.configure(bg = 'Black')
		self.diff_wind.geometry('480x250') ,self.diff_wind.resizable(0,0) , self.diff_wind.title('Difficulty Level')
		Label(self.diff_wind,bg='Black').pack()
		easy = Button(self.diff_wind , text = 'Easy', bg = 'seagreen3',fg='black' , width = 10 ,font = ('veredana italic' , 12, 'bold'),command = lambda : self.set_level('Easy') )
		hard = Button(self.diff_wind , text = 'Hard', bg = 'seagreen3',fg='black' , width = 10 ,font = ('veredana italic' , 12, 'bold'),command = lambda : self.set_level('Hard'))
		insane = Button(self.diff_wind , text = 'Insane', bg = 'seagreen3',fg='black', width = 10 , font = ('veredana italic' , 12, 'bold'),command = lambda : self.set_level('Insane'))
		easy.pack(pady=5 , ipadx = 50 , ipady = 10) , hard.pack(pady=5 , ipadx = 50 , ipady = 10) , insane.pack(pady=5 , ipadx = 50 , ipady = 10)
		easy.bind('<Enter>' , lambda event, bt_this = easy : on_enter(event ,  bt_this ) ) 
		easy.bind('<Leave>' ,  lambda event, bt_this = easy: on_leave( event , bt_this ) ) 		
		hard.bind('<Enter>' , lambda event, bt_this = hard : on_enter(event ,  bt_this ) ) 
		hard.bind('<Leave>' ,  lambda event, bt_this = hard: on_leave( event , bt_this ) ) 		
		insane.bind('<Enter>' , lambda event, bt_this = insane : on_enter(event ,  bt_this ) ) 
		insane.bind('<Leave>' ,  lambda event, bt_this = insane: on_leave( event , bt_this ) ) 		

	
	def set_level(self , txt):
		if txt == 'Easy' : 
			Intro.diff_level = Intro.inverted_dic['--Easy--']
			messagebox.showinfo('Set' , 'Difficulty set to Easy' , parent = self.diff_wind) ,self.diff_wind.destroy()
		elif txt == 'Hard' : 
			Intro.diff_level = Intro.inverted_dic['--Hard--']
			messagebox.showinfo('Set' , 'Difficulty set to Hard' , parent = self.diff_wind) , self.diff_wind.destroy()
		elif txt == 'Insane' : 
			Intro.diff_level = Intro.inverted_dic['--Insane--']
			messagebox.showinfo('Set' , 'Difficulty set to Insane' , parent = self.diff_wind) , self.diff_wind.destroy()

	def __repr__(self):
		return f'----Intro of Class----\nThis class holds GUI for first intro window\nIt has buttons that starts game and show instructions as well as difficulty level\n----Doc---\n{ Intro.__dic__ }'				
# ############### Utility Functions ################ #

def show_grid(root,  parent , specify = False ):
	counter = 0 
	for i in range(8):
		for j in range(8):
			if specify == False: Main.lis_player.append( Create(root , i , j  , '' , 'White' , 'Yellow' ,  counter , parent) )			
			if specify == True: Main.lis_comp.append( Create(root , i , j  , '' , 'White' , 'Yellow' ,  (counter+65) , parent) )
			counter+=1

def start_place():
	check  , count = 0 , 0
	if Main.flag == False:
		for i in Main.lis_player:
			if i.get_bg == 'White':check+=1
			if i.get_bg == 'Red':count+=1 				
		if check == 64:
			messagebox.showinfo('Alert' , ' Place YOUR SHIPS KINDLY !  ')
			return True
		rec = random.sample(range( 0 , 64 ) , count )
		y = list(map( lambda x :  x+65  , rec)  )
		for i in y:
			for j in Main.lis_comp:
				if j.give_id == i:
					j.place_enemy()
		Create.player_health ,  Create.computer_health = count , count			
		count = 0

		Main.player_health['text'] = f'Your-Health : {Create.player_health}'
		Main.computer_health['text'] = f'Comp-Health : {Create.computer_health}'	
		Main.flag = True
		messagebox.showinfo('READY' , f'ALL-SET.!!\n You are playing in "{ Intro.dic[Intro.diff_level] }" mode  Click "OK" to start game' )

 
def play(file_name):
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(loops=0)

def on_enter(e , bt):
   bt.config(background='OrangeRed3', foreground= "white" , cursor = 'hand2')

def on_leave(e  , bt , bg_color = 'seagreen3'):
   bt.config(background= bg_color, foreground= 'black' , cursor = 'hand2')



# ######################### MAIN PROGRAMM ######################### #

if __name__ == '__main__':
	
	sec , minu , flag= 0 , 0 , True
	pygame.mixer.init()
	crr_path = os.getcwd()
	dirs = [ each for each in os.listdir(crr_path) if os.path.isdir(each) ]
	if 'Sounds' in dirs : 
		files = [ f'Sounds/{each}' for each in os.listdir(f'{crr_path}/Sounds') ]
		exp_sound , shot_sound  = 'Sounds/exp.wav' , 'Sounds/shot.mp3'
		if exp_sound in files and shot_sound in files : 
			Intro()
		else : 
			root_msg = Tk()
			root_msg.withdraw()
			messagebox.showerror("Error", f'The files  "{exp_sound}"  and  "{shot_sound}"  doesnt exist in Sounds directory')
	else : 
		root_msg = Tk()
		root_msg.withdraw()
		messagebox.showerror("Error", f'The directory named "Sound" doesnt exist :) ')
			

