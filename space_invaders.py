#create a screen
#python 3
#o create more enenmies we use a  LIST
import turtle
import os
import math

mainscreen=turtle.Screen()  
mainscreen.bgcolor("orange")
mainscreen.title("Team 9")

#  **** DRAW BORDER ****
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()

border_pen.pensize(3)

for side in range(4):    #border drawing
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()   #border drawing ended

#   **** CREATE  THE PLAYER  ******

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()         
player.speed(0)               #max speed of turtle , but player doesnt move
player.setposition(0, -250)   # central position is (0,0)
player.setheading(90)        #player facing to 90 degree
      
playerspeed = 40      #player speed
 
#  **** CREATE ENEMY *****

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed=3
#  *** CHOOSE A NUMBER OF ENEMIES
number_of_enemies = 5
# Create an empty list
enemies = []

# Add enemies to the List
for i in range(number_of_enemies)


# *** CREATE PLAYER BULLETS ****

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup() 
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
# *** bullet state ***
# ready
# fire - bulllet is firing
bulletstate = "ready"

# PLAYER MOVEMENT
# CREATE FUNCTIONS FOR MOVING LEFT & RIGHT 

def move_left():       # at start my player is at x=0 and y =250
    x = player.xcor()   
    x-= playerspeed      # for every press of a key it moves by 15 coordinates  
    if x < -280:
       x = - 280                    # but it moves beyond the boundaries
    player.setx(x)

def move_right():
    x=player.xcor()
    x += playerspeed
    if x > +280:
        x = + 280
    player.setx(x)
def move_up():
    y= player.ycor()
    y+= playerspeed
    if y > +280:
        y = 280
    player.sety(y)
def move_down():
    y=player.ycor()
    y-=playerspeed
    if y < -280:
        y = -280
    player.sety(y)

# BULLET MOVEMNT

def fire_bullet():
    # bullet state as global
    global bulletstate         # any chages done here will reflect outside as well
    if bulletstate == "ready":  # MOVE THE BULLET FROM THE TOP OF THE PLAYER 
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
    # these below 2 lines will move bullet by 30 positions which is bullet speed
    # i want to bullet to keep moving contioniusly if once i press space button
    # y += bulletspeed
    # bullet.sety(y)
        bullet.showturtle()

def ifcollision(t1, t2):

    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True 
    else:
        return False


# *** CREATE KEYBOARD BINDINGS ***

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(fire_bullet, "space") 

# *** MAIN GAME LOOP ***

while True:
    
#MOVE THE ENEMY

    x = enemy.xcor()
    x  += enemyspeed
    enemy.setx(x)     #enemy moves bcz we are dynamically changingh x coordinate
                      # and moves contionously bcz of while True loop
    
#ENEMY MOVING OUT OF THE SCREEN, SO REVERSE IT 
    if x > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if x < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

# MOVE THE BULLET
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)    # bullet will move contionously when game starts but it is invisble bcz of bullet                               .hideturtle() function 
# CHECK IF BULLET MOVES OUR OF THE BORDER
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

# CHECK THE COLLISION
    if ifcollision(bullet, enemy):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #RESET THE ENEMY
        enemy.setposition(-200, 250)
    if ifcollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("GAME OVER")
        break
         
#delay=input("press enter to finish.>") 
#turtle.done()# 


#window await
mainscreen.mainloop()




