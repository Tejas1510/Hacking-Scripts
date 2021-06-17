import os
import turtle
from tkinter import messagebox

wn = turtle.Screen()
wn.title("Ping-Pong by Rutuj Runwal")
wn.bgcolor("teal")
wn.setup(width=800, height=600)
wn.tracer(2)  

#Display a messagebox at the start to make user's familiar with controls
messagebox.showinfo("Welcome!","Welcome to Ping-Pong!\nThis is a two player game\nThe first player uses W-S-A-D keys to move the paddle\nThe second player uses arrow-keys\nHave fun 🔥")

# prompt user for names
player1 = turtle.textinput("Player1", "Enter your Name:")
while(player1==None or player1==""):
    messagebox.showinfo("Enter Name","Please specify player1 name in the prompt:")
    player1 = turtle.textinput("Player2", "Enter your Name:")
player2 = turtle.textinput("Personal Detail", "Enter your Name:")
while(player2==None or player2==""):
    messagebox.showinfo("Enter Name","Please specify player2 name in the prompt:")
    player2 = turtle.textinput("Personal Detail", "Enter your Name:")

messagebox.showinfo("Game Begins","The match is about to start\n" + str(player1)+ " VS " + str(player2))

# Score - Initially 0
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
# ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0  {}: 0".format(player1, player2), align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # up when w is pressed
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Main game loop
while True:
    wn.update()  # every time the loop runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(player1, score_a, player2, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(player1, score_a, player2, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # Paddle and ball collisions
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

