from tkinter import *
import time
import random
import pyglet

#Splash Screen For the Game
animation=pyglet.image.load_animation('Bounce Ball_SplashScreen.gif')
animSprite=pyglet.sprite.Sprite(animation)
w=animSprite.width
h=animSprite.height

win=pyglet.window.Window(width=w,height=h,style='borderless')
win.set_location(200,100)

r,g,b,alpha=0.5,0.5,0.8,0.5
pyglet.gl.glClearColor(r,g,b,alpha)
@win.event

def on_draw():
	win.clear()
	animSprite.draw()

def close(event):
	win.close()

pyglet.clock.schedule_once(close,5.0)

pyglet.app.run()

root = Tk()
root.title("Bounce Ball")
root.geometry("550x600")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)
score = Label(height=50, width=80, text="Score: 00", font="Consolas 14 bold")
score.pack(side="left")
root.update()

#Added the logo to application
l=PhotoImage(file="Bounce Ball_Logo.png")
root.iconphoto(False,l)

#Class function defines the complete functioning of the game
class Ball:
    def __init__(self, canvas, color, paddle, bricks, score):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1)
        self.canvas.move(self.id, 230, 461)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        self.x = start[0]
        self.y = -start[0]
        self.canvas.move(self.id, self.x, self.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

    def brick_hit(self, pos):
        for brick_line in self.bricks:
            for brick in brick_line:
                brick_pos = self.canvas.coords(brick.id)
                try:
                    if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                        if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                            canvas.bell()
                            self.hit += 1
                            self.score.configure(text="Score: " + str(self.hit))
                            self.canvas.delete(brick.id)
                            return True
                except:
                    continue
        return False

    def paddle_hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        if self.brick_hit(pos):
            self.y = start[0]
        if pos[1] <= 0:
            self.y = start[0]
        if pos[3] >= self.canvas_height:
            self.bottom_hit = True
        if pos[0] <= 0:
            self.x = start[0]
        if pos[2] >= self.canvas_width:
            self.x = -start[0]
        if self.paddle_hit(pos):
            self.y = -start[0]


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 485)
        self.x = 0
        self.pausec = 0
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        self.canvas.bind_all("<space>", self.pauser)

    def draw(self):
        pos = self.canvas.coords(self.id)
        # print(pos)
        if pos[0] + self.x <= 0:
            self.x = 0
        if pos[2] + self.x >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

#For left, right and space key
    def turn_left(self, event):
        self.x = -3.5

    def turn_right(self, event):
        self.x = 3.5

    def pauser(self, event):
        self.pausec += 1
        if self.pausec == 2:
            self.pausec = 0

class Bricks:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color, width=2)

playing = False

#Main code to run the game
def start_game(event):
    global playing
    if playing is False:
        playing = True
        score.configure(text="Your Score: 00")
        canvas.delete("all")
        #Colours of the balls and brick
        BALL_COLOR = ["red", "yellow", "white"]
        BRICK_COLOR = ["PeachPuff3", "dark grey", "rosy brown", "light goldenrod yellow", "turquoise3", "salmon",
                       "light steel blue", "dark khaki", "pale violet red", "orchid", "tan", "MistyRose2",
                       "DodgerBlue4", "wheat2", "RosyBrown2", "bisque3", "DarkSeaGreen1"]
        random.shuffle(BALL_COLOR)
        paddle = Paddle(canvas, "blue")
        bricks = []
        for i in range(0, 5):
            b = []
            for j in range(0, 19):
                random.shuffle(BRICK_COLOR)
                tmp = Bricks(canvas, BRICK_COLOR[0])
                b.append(tmp)
            bricks.append(b)

        for i in range(0,5):
            for j in range(0,19):
                canvas.move(bricks[i][j].id,25*j,25*i)

        ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score)
        root.update_idletasks()
        root.update()

        time.sleep(1)
        while 1:
            if paddle.pausec != 1:
                try:
                    canvas.delete(m)
                    del m
                except:
                    pass
                if not ball.bottom_hit:
                    ball.draw()
                    paddle.draw()
                    root.update_idletasks()
                    root.update()
                    time.sleep(0.01)
                    #If score is 95 a message will be displayed.
                    if ball.hit == 95:
                        canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Consolas 24 ")
                        root.update_idletasks()
                        root.update()
                        playing = False
                        break
                else:
                    #Game Over will be displayed when the ball hits the bottom of frame
                    canvas.create_text(250, 250, text="GAME OVER!!", fill="red", font="Consolas 24 ")
                    root.update_idletasks()
                    root.update()
                    playing = False
                    break
            else:
                try:
                    if m == None: pass
                except:
                    #Using space key a person can pause the game
                    m = canvas.create_text(250, 250, text="PAUSE!!", fill="pink", font="Consolas 26 ")
                root.update_idletasks()
                root.update()

root.bind_all("<Return>", start_game)
canvas.create_text(250, 250, text="Press Enter To Start The Game!!",fill="red",font="Consolas 20")
j = canvas.find_all()
root.mainloop()
