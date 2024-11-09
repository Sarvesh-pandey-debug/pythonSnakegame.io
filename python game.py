import turtle as trt
import random
import time
import tkinter


# ALL ABOUT SCREEN DESIGNING


delay = 0.1
sc=0
hs=0
bodies=[]
#CreatingScreen
s=trt.Screen()
s.title("Snake Game")
s.bgcolor("light pink")
s.setup(width = 600, height = 600)  # ScreenSize

#Creating snake head Head
head=trt.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"

#Creating Food for snake

food=trt.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.ht()                # for hiding a turtle
food.goto(150,200)
food.st()                # st =  for showing a turtle


#Creating Score Board
sb=trt.Turtle()
sb.penup()
sb.ht()
sb.goto(-250,350)
sb.write("Score: 0  |  Highest Score: 0") # to print a score on the screen for the first time

#Creating function for moving in all direction

def moveUp():
    if head.direction!="down":
        head.direction="up"

def moveDown():
    if head.direction!="up":
        head.direction="down"



def moveRight():
    if head.direction!="left":
        head.direction="right"

def moveLeft():
    if head.direction!="right":
        head.direction="left"

def moveStop():
    head.direction="stop"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)      # agr head ka direction up hai to y me dal do y cordinate ki value (snake kis position pe hai 0 10 ...etc) and then head.set y function me y ko bdha do 20+ se
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)





# STEP 2  EVENT HANDLING  (SARE FUNCTION OR CLASS KA USE KARENGE KI UNKA KAM JO HAI VO KARE)

s.listen()     # screen kya karega listen() me batana padega
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveRight,"Right")
s.onkey(moveLeft,"Left")
s.onkey(moveStop,"space")

#Main game loop

while True:
    s.update()  # to update the screen

    # check collision with border

    if head.xcor()>290:             # agar head 290 pe pahuch gya to phir jab badhega 20+ hoga to 310 ho jayega or border se lad jayega isliye ise handle kiya -290 pe reopen hoga head
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)

    #check collision with food

    if head.distance(food)<20:   # agr head apna food se 20 ... se doori pe raha to usko vaha se modana padega kahi random jagah  nahi to collision ho jayega khud se or isiliye random lib use kiye hai
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # increase the body of snake (jab snake food khayega to uski speed or size to badhani pdegi )
        body=trt.Turtle()   # making new object
        body.speed(0)
        body.penup()
        body.shape("triangle")
        body.color("yellow")
        bodies.append(body) # append the new body in list


        #handling the score board after snake eat food

        sc=sc+10 # increase the score
        delay=delay-0.001 # increase the speed

        if sc>hs:
            hs=sc     # update highest score
        sb.clear()      # scoreboard ko clear kra lo nahi to ak ke uper ak score ata rahega
        sb.write("score: {}   |   Highest Score: {}".format(sc,hs)) # hs sc ko print kra diye
    # move snake bodies
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()


     # check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.01
            sb.clear()
            sb.write("score: {}  |  Highest Score: {}".format(sc,hs))
    time.sleep(delay)

trt.mainloop()
