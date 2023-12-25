"""
Progammer: Abdallah Abdelaal
Title: toronto-canvas

Short explanation:
This program draws a city skyline of Toronto.

Additional Features used: 
- Used Python With Turtle
"""

#Set up for Canvas
import turtle
t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.setup(1.0, 1.0)
s.bgcolor("orange")


#Sun
t.up()
t.goto(-300,-100)
t.down()
t.lt(90)
t.color("yellow")
t.begin_fill()
for i in range(180):
  t.fd(6)
  t.rt(1)
t.lt(90)
t.end_fill()

#Base
t.up()
t.goto(-300,-100)
t.down()
t.pensize(10)
t.color("black")
t.fd(700)

#BACKGROUND BUILDINGS
t.color("lightgrey")

#Repositioning for First Building
t.up()
t.goto(-250,100)
t.down()
t.pensize(1)

#First building 
t.begin_fill()
t.rt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.end_fill()

#repositioning for second building
t.up()
t.rt(180)
t.fd(115)
t.rt(90)
t.fd(200)
t.lt(180)
t.down()

#Second building
t.begin_fill()
t.fd(200)
t.rt(20)
t.fd(40)
t.rt(70)
t.fd(30)
t.rt(90)
t.fd(240)
t.end_fill()

#Repositioning for third building
t.up()
t.lt(90)
t.fd(15)
t.lt(90)
t.down()

#Third building
t.begin_fill()
t.fd(220)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(220)
t.end_fill()

#repositioning for fourth building
t.up()
t.goto(140,-100)
t.down()

#Fourth building
t.begin_fill()
t.fd(-150)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(75)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(245)
t.end_fill()

#Repositioning for fifth building
t.up()
t.lt(90)
t.fd(30)
t.down()

#Fifth building 
t.begin_fill()
t.fd(100)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(200)
t.end_fill()

#MIDDLEGROUND BUILDINGS 
t.color("darkgrey")

#repositioning for first building
t.up()
t.goto(-235,-100)
t.down()

#First building
t.begin_fill()
t.fd(-120)
t.lt(160)
t.fd(50)
t.rt(70)
t.fd(20)
t.rt(70)
t.fd(50)
t.lt(70)
t.fd(30)
t.lt(90)
t.fd(50)
t.rt(30)
t.fd(20)
t.rt(120)

#Other side of first building
t.fd(20)
t.rt(30)
t.fd(50)
t.lt(90)
t.fd(30)
t.lt(70)
t.fd(50)
t.rt(70)
t.fd(20)
t.rt(70)
t.fd(50)
t.rt(20)
t.fd(120)
t.end_fill()

#Repositioning for second building
t.up()
t.goto(90,-100)
t.down()

#Second building 
t.begin_fill()
t.fd(-180)
t.lt(90)
t.fd(80)
t.rt(90)
t.fd(180)
t.end_fill()
t.lt(90)

#FOREGROUND BUILDINGS
t.color("black")

#First building
t.up()
t.goto(-290,-100)
t.down()
t.pensize(1)
t.lt(90)
t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(100)
t.end_fill()

#Second Building 
t.up()
t.goto(-40,-100)
t.down()
t.begin_fill()
t.rt(180)
t.fd(17)
t.end_fill() 

#Arch for Rogers centre
t.up()
t.goto(-20,-150)
t.down()
t.begin_fill()
for i in range(180):
  t.fd(2)
  t.lt(1)
t.end_fill()

#Left side of Rogers centre
t.up()
t.goto(-228,-100)
t.down()
t.begin_fill()
t.fd(-17)
t.end_fill()

#Hiding bottom of arch
t.up()
t.goto(-290,-100)
t.down()
t.color("orange")
t.begin_fill()
t.fd(100)
t.lt(90)
t.fd(400)
t.lt(90)
t.fd(100)
t.end_fill()

#Hiding right side of Arch
t.begin_fill()
t.up()
t.goto(-30,-100)
t.down()
t.color("grey")
t.fd(20)
t.lt(90)
t.fd(9)
t.lt(90)
t.fd(20)
t.end_fill()

#Hiding left side of Arch
t.up()
t.goto(-229,-100)
t.down()
t.color("darkgrey")
t.rt(180)
t.begin_fill()
t.fd(20)
t.lt(90)
t.fd(6)
t.lt(90)
t.fd(20)
t.end_fill()

#making lines black again
t.color("black")
t.up()
t.goto(-300,-100)
t.down()
t.lt(90)
t.pensize(10)
t.fd(700)

#Repositioning for Third Building
t.pensize(1)
t.up()
t.goto(-20,-100)
t.down()
t.lt(90)

#Third Building
t.begin_fill()
t.fd(160)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(160)
t.end_fill()

#Repositioning for CN Tower
t.up()
t.goto(70,-100)
t.down()

#Base for CN Tower
t.lt(175)
t.begin_fill()
t.fd(300)
t.rt(85)
t.fd(10)
t.rt(85)
t.fd(300)
t.end_fill()

#Bottom side of SkyPod on Cn Tower
t.fd(-300)
t.lt(85)
t.fd(10)
t.fd(-30)
t.begin_fill()
t.fd(30)
for i in range(180):
  t.fd(0.15)
  t.lt(1)

t.fd(30)

for i in range(180):
  t.fd(0.15)
  t.lt(1)
t.end_fill()

t.lt(90)
t.up()
t.fd(17)
t.down()

#Top side of Skypod
t.lt(40)
t.begin_fill()
t.fd(15)
t.lt(50)
t.fd(5)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.lt(50)
t.fd(15)
t.rt(50)
t.fd(30)

#other side of Skypod
t.rt(50)
t.fd(15)
t.lt(50)
t.fd(5)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(5)
t.lt(50)
t.fd(15)
t.end_fill()

#Repositioning for spike on top of CN Tower
t.seth(90)
t.up()
t.fd(33)
t.lt(90)
t.fd(30)
t.down()

#Spike on top of CN Tower
t.begin_fill()
t.fd(-13)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(4)
t.rt(90)
t.fd(2)
t.rt(90)
t.fd(4)
t.lt(87)
t.fd(50)

t.rt(174)
t.fd(50)
t.lt(87)
t.fd(4)
t.rt(90)
t.fd(2)
t.rt(90)
t.fd(4)
t.lt(90)
t.fd(5)
t.end_fill()

#Repositioning for Fifth building
t.up()
t.fd(350)
t.lt(90)
t.fd(50)
t.lt(90)
t.down()

#Fifth Building
t.begin_fill()
t.fd(125)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(15)
t.rt(90)
t.fd(5)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(45)
t.fd(5)
t.lt(45)
t.fd(5)
t.rt(90)
t.fd(5)


#Other side of Fifth Building
t.rt(90)
t.fd(5)
t.lt(45)
t.fd(5)
t.rt(45)
t.fd(10)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(15)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(20)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(125)
t.end_fill()

#Repositioning for sixth building
t.up()
t.lt(90)
t.fd(15)
t.lt(90)
t.down()

#sixth Building
t.begin_fill()
t.fd(140)
t.rt(90)
t.fd(20)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(15)
t.rt(90)
t.fd(20)
t.lt(90)
t.fd(15)
t.rt(90)
t.fd(15)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(10)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(140)
t.end_fill()

#Repositioning for Seventh Building 
t.begin_fill()
t.up()
t.lt(90)
t.fd(15)
t.lt(90)
t.down()
t.fd(100)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(100)
t.end_fill()

#Border for "TORONTO"
t.up()
t.goto(-300,-100)
t.down()
t.pensize(10)
t.begin_fill()
t.fd(125)
t.lt(90)
t.fd(700)
t.lt(90)
t.fd(125)
t.end_fill()

#"TORONTO"
t.up()
t.goto(-300,-250)
t.down()
t.color("white")
t.write("TORONTO",font=("Times New Roman", 95, "normal"))

t.hideturtle()

input("Hit enter.")