import turtle
import math
import time


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pixel Destroyer")

border_pen      = turtle.Turtle()
player_one      = turtle.Turtle()
player_two      = turtle.Turtle()
bullet_plyone   = turtle.Turtle()
bullet_plytwo   = turtle.Turtle()

#row 1
enemy           = turtle.Turtle()
enemy_one       = turtle.Turtle()
enemy_two       = turtle.Turtle()
enemy_three     = turtle.Turtle()
enemy_four      = turtle.Turtle()

#row 2
enemy_five   = turtle.Turtle()
enemy_six    = turtle.Turtle()
enemy_seven  = turtle.Turtle()
enemy_eight  = turtle.Turtle()
enemy_nine   = turtle.Turtle()

#border pen
if 0 == 0:
    border_pen.setposition(-300, -300)
    border_pen.color("white")
    border_pen.penup()
    border_pen.speed(2)
    border_pen.pendown()
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

#player one
if 0 == 0:
 player_one.setposition(0, 250)
 player_one.speed(0)
 player_one.shape("square")
 player_one.color("blue")
 player_one.penup()### #   #\\\\////
#player two
if 0 == 0:
 player_two.setposition(0, -250)
 player_two.shape("square")
 player_two.color("red")
 player_two.penup()

#bullet player one
if 0 == 0:
    bullet_plyone.color("yellow")
    bullet_plyone.speed(0)
    bullet_plyone.penup()
    bullet_plyone.pensize(3)
    bullet_plyone.setheading(270)
    bullet_plyone.hideturtle()
    bullet_plyone.setposition(0, 250)
#bullet player two
if 0 == 0:
    bullet_plytwo.color("pink")
    bullet_plytwo.speed(0)
    bullet_plytwo.penup()
    bullet_plytwo.pensize(3)
    bullet_plytwo.setheading(90)
    bullet_plytwo.hideturtle()
    bullet_plytwo.setposition(0, -250 )

#enemies
if 0 == 0:
    enemy.setposition(-280, 0)
    enemy.shape("circle")
    enemy.color("green")
    enemy.penup()

    enemy_one.setposition(-250, 0)
    enemy_one.shape("circle")
    enemy_one.color("green")
    enemy_one.penup()

    enemy_two.setposition(-220, 0)
    enemy_two.shape("circle")
    enemy_two.color("green")
    enemy_two.penup()

    enemy_three.setposition(-190, 0)
    enemy_three.shape("circle")
    enemy_three.color("green")
    enemy_three.penup()

    enemy_four.setposition(-160, 0)
    enemy_four.shape("circle")
    enemy_four.color("green")
    enemy_four.penup()
#--------------------------------------
    enemy_five.setposition(-280, 30)
    enemy_five.shape("circle")
    enemy_five.color("green")
    enemy_five.penup()

    enemy_six.setposition(-250, 30)
    enemy_six.shape("circle")
    enemy_six.color("green")
    enemy_six.penup()

    enemy_seven.setposition(-220, 30)
    enemy_seven.shape("circle")
    enemy_seven.color("green")
    enemy_seven.penup()

    enemy_eight.setposition(-190, 30)
    enemy_eight.shape("circle")
    enemy_eight.color("green")
    enemy_eight.penup()

    enemy_nine.setposition(-160, 30)
    enemy_nine.shape("circle")
    enemy_nine.color("green")
    enemy_nine.penup()

#speed for turtles
if 0 == 0:
    player_one_speed     = 15
    player_two_speed     = 15
    #------------------------
    enemy_speed          = 2
    enemy_one_speed      = 2
    enemy_two_speed      = 2
    enemy_three_speed    = 2
    enemy_four_speed     = 2

    enemy_five_speed     = 2
    enemy_six_speed      = 2
    enemy_seven_speed    = 2
    enemy_eight_speed    = 2
    enemy_nine_speed     = 2
    #------------------------
    bullet_plyone_speed  = 30
    bullet_plytwo_speed  = 30

#states
if 0 == 0:
    bullet_plyone_state = "ready"
    bullet_plytwo_state = "ready"

def move_plyone_left():
    x = player_one.xcor()
    x -= player_one_speed
    if x < - 280:
        x = -280
    player_one.setx(x)
def move_plyone_right():
    x = player_one.xcor()
    x += player_one_speed
    if x > 280:
        x = 280
    player_one.setx(x)
def move_plytwo_left():
    x = player_two.xcor()
    x -= player_two_speed
    if x < -280:
       x = -280
    player_two.setx(x)
def move_plytwo_right():
    x = player_two.xcor()
    x += player_two_speed
    if x > 280:
       x = 280
    player_two.setx(x)
def fire_plyone():
    global bullet_plyone_state
    if bullet_plyone_state == "ready":
     bullet_plyone_state = "fire"
     x = player_one.xcor()
     y = player_one.ycor() - 10
     bullet_plyone.setposition(x,y)
     bullet_plyone.showturtle()
def fire_plytwo():
   global bullet_plytwo_state
   if bullet_plytwo_state == "ready":
       bullet_plytwo_state = "fire"
       x = player_two.xcor()
       y = player_two.ycor() +10
       bullet_plytwo.setposition(x, y)
       bullet_plytwo.showturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(fire_plyone, "s")
turtle.onkey(move_plyone_left, "a")
turtle.onkey(move_plyone_right, "d")
turtle.onkey(move_plytwo_left, "Left")
turtle.onkey(move_plytwo_right, "Right")
turtle.onkey(fire_plytwo,"Down")

while True:

   if bullet_plyone_state == "fire":
       y = bullet_plyone.ycor()
       y -= bullet_plyone_speed
       bullet_plyone.sety(y)
   if bullet_plyone.ycor() < -300:
      bullet_plyone.hideturtle()
      bullet_plyone_state = "ready"

   if bullet_plytwo_state == "fire":
       y = bullet_plytwo.ycor()
       y += bullet_plytwo_speed
       bullet_plytwo.sety(y)
   if bullet_plytwo.ycor() > 300:
       bullet_plytwo.hideturtle()
       bullet_plytwo_state = "ready"

#--------------------------------
   x = enemy.xcor()
   x += enemy_speed
   enemy.setx(x)
   if x > 280:
      enemy_speed *= -1
      enemy.setx(x)
   if x < -280:
      enemy_speed *= -1
      enemy.setx(x)
#--------------------------------
   x_one = enemy_one.xcor()
   x_one += enemy_one_speed
   enemy_one.setx(x_one)
   if x_one > 280:
      enemy_one_speed *= -1
      enemy_one.setx(x_one)
   if x_one < -280:
      enemy_one_speed *= -1
      enemy_one.setx(x_one)
#--------------------------------
   x_two = enemy_two.xcor()
   x_two += enemy_two_speed
   enemy_two.setx(x_two)
   if x_two > 280:
      enemy_two_speed *= -1
      enemy_two.setx(x_two)
   if x_two < -280:
      enemy_two_speed *= -1
      enemy_two.setx(x_two)
#--------------------------------
   x_three = enemy_three.xcor()
   x_three += enemy_three_speed
   enemy_three.setx(x_three)
   if x_three > 280:
       enemy_three_speed *= -1
       enemy_three.setx(x_three)
   if x_three < -280:
       enemy_three_speed *= -1
       enemy_three.setx(x_three)
# --------------------------------
   x_four = enemy_four.xcor()
   x_four += enemy_four_speed
   enemy_four.setx(x_four)
   if x_four > 280:
       enemy_four_speed *= -1
       enemy_four.setx(x_four)
   if x_four < -280:
       enemy_four_speed *= -1
       enemy_four.setx(x_four)
# --------------------------------
   x_five = enemy_five.xcor()
   x_five += enemy_five_speed
   enemy_five.setx(x_five)
   if x_five > 280:
       enemy_five_speed *= -1
       enemy_five.setx(x_five)
   if x_five < -280:
       enemy_five_speed *= -1
       enemy_five.setx(x_five)
# --------------------------------
   x_six = enemy_six.xcor()
   x_six += enemy_six_speed
   enemy_six.setx(x_six)
   if x_six > 280:
       enemy_six_speed *= -1
       enemy_six.setx(x_six)
   if x_six < -280:
       enemy_six_speed *= -1
       enemy_six.setx(x_six)
# --------------------------------
   x_seven = enemy_seven.xcor()
   x_seven += enemy_seven_speed
   enemy_seven.setx(x_seven)
   if x_seven > 280:
       enemy_seven_speed *= -1
       enemy_seven.setx(x)
   if x_seven < -280:
       enemy_seven_speed *= -1
       enemy_seven.setx(x)
# --------------------------------
   x_eight = enemy_eight.xcor()
   x_eight += enemy_eight_speed
   enemy_eight.setx(x_eight)
   if x_eight > 280:
       enemy_eight_speed *= -1
       enemy_eight.setx(x_eight)
   if x_eight < -280:
       enemy_eight_speed *= -1
       enemy_eight.setx(x_eight)
 # --------------------------------
   x_nine = enemy_nine.xcor()
   x_nine += enemy_nine_speed
   enemy_nine.setx(x_nine)
   if x_nine > 280:
       enemy_nine_speed *= -1
       enemy_nine.setx(x_nine)
   if x_nine < -280:
       enemy_nine_speed *= -1
       enemy_nine.setx(x_nine)
   # --------------------------------


   if isCollision(bullet_plyone, player_two):
       player_two.hideturtle()
       enemy.hideturtle()
       enemy_one.hideturtle()
       enemy_two.hideturtle()
       enemy_three.hideturtle()
       enemy_four.hideturtle()
       turtle.color("magenta")
       turtle.hideturtle()
       turtle.write("Game Over",  move=False, align="Center", font=("Arial", 30, "bold"))
       time.sleep(3)
       turtle.clear()
       turtle.write("Player One Winner", move=False, align="Center", font=("Arial", 30, "bold"))
   if isCollision(bullet_plytwo, player_one):
       player_one.hideturtle()
       enemy.hideturtle()
       enemy_one.hideturtle()
       enemy_two.hideturtle()
       enemy_three.hideturtle()
       enemy_four.hideturtle()
       turtle.color("magenta")
       turtle.hideturtle()
       turtle.write("Game Over", move=False, align="Center", font=("Arial", 30, "bold"))
       time.sleep(3)
       turtle.clear()
       turtle.write("Plyer Two Winner", move=False, align="Center", font=("Arial", 30, "bold"))

   if isCollision(bullet_plyone,enemy):
    bullet_plyone.hideturtle()

    if enemy.isvisible():
      a=1
      b=1
      c=a+b
      bullet_plyone.setposition(300, 300)
    else:
      bullet_plyone.showturtle()
    enemy.hideturtle()
   if isCollision(bullet_plyone,enemy_one):
       bullet_plyone.hideturtle()

       if enemy_one.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plyone.setposition(300, 300)
       else:
           bullet_plyone.showturtle()
       enemy_one.hideturtle()
   if isCollision(bullet_plyone, enemy_two):
       bullet_plyone.hideturtle()

       if enemy_two.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plyone.setposition(300, 300)
       else:
           bullet_plyone.showturtle()
       enemy_two.hideturtle()
   if isCollision(bullet_plyone,enemy_three):
       bullet_plyone.hideturtle()

       if enemy_three.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plyone.setposition(300, 300)
       else:
           bullet_plyone.showturtle()
       enemy_three.hideturtle()
   if isCollision(bullet_plyone,enemy_four):
       bullet_plyone.hideturtle()

       if enemy_four.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plyone.setposition(300, 300)
       else:
           bullet_plyone.showturtle()
       enemy_four.hideturtle()
   if isCollision(bullet_plyone, enemy_five):
       bullet_plyone.hideturtle()

       if enemy_five.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plyone.setposition(300, 300)
       else:
           bullet_plyone.showturtle()
       enemy_five.hideturtle()
   if isCollision(bullet_plyone, enemy_six):
    bullet_plyone.hideturtle()

    if enemy_six.isvisible():
         a = 1
         b = 1
         c = a + b
         bullet_plyone.setposition(300, 300)
    else:
         bullet_plyone.showturtle()

    enemy_six.hideturtle()
   if isCollision(bullet_plyone, enemy_seven):
    bullet_plyone.hideturtle()

    if enemy_seven.isvisible():
         a = 1
         b = 1
         c = a + b
         bullet_plyone.setposition(300, 300)
    else:
         bullet_plyone.showturtle()

    enemy_seven.hideturtle()
   if isCollision(bullet_plyone, enemy_eight):
        bullet_plyone.hideturtle()

        if enemy_eight.isvisible():
            a = 1
            b = 1
            c = a + b
            bullet_plyone.setposition(300, 300)
        else:
            bullet_plyone.showturtle()

        enemy_eight.hideturtle()
   if isCollision(bullet_plyone, enemy_nine):
       bullet_plyone.hideturtle()

       if enemy_nine.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plyone.setposition(300, 300)
       else:
           bullet_plyone.showturtle()

       enemy_nine.hideturtle()

   if isCollision(bullet_plytwo, enemy):
       bullet_plytwo.hideturtle()
       if enemy.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()
       enemy.hideturtle()
   if isCollision(bullet_plytwo, enemy_one):

       bullet_plytwo.hideturtle()

       if enemy_one.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()
       enemy_one.hideturtle()
   if isCollision(bullet_plytwo, enemy_two):

       bullet_plytwo.hideturtle()

       if enemy_two.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()
       enemy_two.hideturtle()
   if isCollision(bullet_plytwo, enemy_three):
       bullet_plytwo.hideturtle()

       if enemy_three.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()
       enemy_three.hideturtle()
   if isCollision(bullet_plytwo, enemy_four):
       bullet_plytwo.hideturtle()

       if enemy_four.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()
       enemy_four.hideturtle()
   if isCollision(bullet_plytwo, enemy_five):
       bullet_plytwo.hideturtle()

       if enemy_five.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()
       enemy_five.hideturtle()
   if isCollision(bullet_plytwo, enemy_six):
       bullet_plytwo.hideturtle()

       if enemy_six.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()

       enemy_six.hideturtle()
   if isCollision(bullet_plytwo, enemy_seven):
       bullet_plytwo.hideturtle()

       if enemy_seven.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()

       enemy_seven.hideturtle()
   if isCollision(bullet_plytwo, enemy_eight):
       bullet_plytwo.hideturtle()

       if enemy_eight.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()

       enemy_eight.hideturtle()
   if isCollision(bullet_plytwo, enemy_nine):
       bullet_plytwo.hideturtle()

       if enemy_nine.isvisible():
           a = 1
           b = 1
           c = a + b
           bullet_plytwo.setposition(300, 300)
       else:
           bullet_plytwo.showturtle()

       enemy_nine.hideturtle()




turtle.mainloop()
