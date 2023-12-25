"""
Progammer: Abdallah Abdelaal
Title: slot-machine
Created on: January 28, 2021
Last Edited on: February 4,2021

Short explanation of game:
This slot machine game is a betting game. It is a betting a game where you have to get 3 of the same symbols in a row to earn money. 

Additional Features used: 
- Used Python With Turtle
"""
#Imports
import random
import time
import turtle

#List of colours 
colours = ["white", "green", "purple", "red", "yellow"]

#Turtle setup
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor(colours[2])
t.hideturtle()
t.speed(0)

#Introduction to game
input("Welcome to the slot machine game! Press any button/key to continue.")
print("")

input("In the slot machine game, you will roll 3 slots of symbols and you will have to try to roll the same symbol in each slot. Press any button/key to continue.")
print("")

input("In order to play this game, you have to bet $20. If you happen to roll 3 of the same symbol, you get a cash prize. Here are the different winnings you could earn (these do not include the $20 you bet meaning you also get your $20 back if you win):")

print("[#][#][#] = $20")
print("[$][$][$] = $50")
print("[7][7][7] = $100")

print("If you do not get any of these winnings, the $20 you bet is gone.")
print("")
input("Are you ready to start playing? Press any button/key to start. ")
print("")


#Starting variables
money = 100
replay = True

#Game setup
while(replay == True and money > 0):
  money = money - 20

  #Transitioning to borders of slots
  t.color(colours[4])
  t.up()
  t.goto(-390,-140)
  t.down()

  #Borders of slots
  t.begin_fill()
  t.fd(780)
  t.lt(90)
  t.fd(280)
  t.lt(90)
  t.fd(780)
  t.lt(90)
  t.fd(280)
  t.end_fill()
  t.lt(90)

  #Transitioning to slots
  t.color(colours[0])
  t.up()
  t.goto(-370,-120)
  t.down()

  #Slots 
  t.begin_fill()
  t.fd(740)
  t.lt(90)
  t.fd(240)
  t.lt(90)
  t.fd(740)
  t.lt(90)
  t.fd(240)
  t.end_fill()
  t.seth(0)

  #Separation of slots
  t.color(colours[4])
  for s in range(-135,116,250):
    t.up()
    t.goto(s,-120)
    t.down()
    t.seth(90)
    t.begin_fill()
    t.fd(240)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(240)
    t.rt(90)
    t.fd(20)
    t.end_fill()
    t.seth(0)

  #Game
  for i in range(1,4):
    input("Click enter to roll the slot")
    print("Rolling...")
    time.sleep(3)
    roll = random.randint(1,3)
    x = 250*i
    totalroll = 1

    #If rolled a dollar sign
    if (roll == 1):
      totalroll = totalroll*1
      if (i == 1):
        slot1 = totalroll
      if (i == 2):
        slot2 = totalroll
      if (i == 3):
        slot3 = totalroll

      #transition to slot
      t.color(colours[1])
      t.up()
      t.goto((x-520),-100)
      t.down()

      #drawing stick in $
      t.begin_fill()
      t.fd(20)
      t.lt(90)
      t.fd(200)
      t.lt(90)
      t.fd(20)
      t.lt(90)
      t.fd(200)
      t.end_fill()

      #Repositioning for S in $
      t.seth(0)
      t.up()
      t.goto((x-560),-40)
      t.down()

      #drawing bottom half of S
      t.begin_fill()
      t.fd(20)
      t.rt(90)
      for a in range(270):
        t.fd(0.5)
        t.lt(1)
      t.rt(90)
      t.fd(20)
      t.rt(90)
      for b in range(270):
        t.fd(0.85)
        t.rt(1)
      t.end_fill()

      #repositioning for top half of S
      t.rt(180)
      t.up()
      for c in range(270):
        t.fd(0.85)
        t.lt(1)
      t.down()

      #Drawing top half of S
      t.begin_fill()
      for d in range(270):
        t.fd(0.5)
        t.rt(1)
      t.lt(90)
      t.fd(20)
      t.lt(90)
      for e in range(270):
        t.fd(0.85)
        t.lt(1)
      t.end_fill()
      t.seth(0)

    #If rolled a 7
    elif(roll == 2):
      totalroll = totalroll*2
      if (i == 1):
        slot1 = totalroll
      if (i == 2):
        slot2 = totalroll
      if (i == 3):
        slot3 = totalroll

      #transition to slot
      t.color(colours[2])
      t.up()
      t.goto(x-590,100)
      t.down()
      t.seth(0)

      #Drawing
      t.begin_fill()
      t.fd(180)
      t.rt(90)
      t.fd(40)
      t.rt(20)
      t.fd(175)
      t.rt(70)
      t.fd(40)
      t.rt(110)
      t.fd(175)
      t.lt(110)
      t.fd(140)
      t.rt(90)
      t.fd(40)
      t.end_fill()
      t.seth(0)

    #If rolled a hashtag
    else:
      totalroll = totalroll*3
      if (i == 1):
        slot1 = totalroll
      if (i == 2):
        slot2 = totalroll
      if (i == 3):
        slot3 = totalroll

      #transition to slot
      t.color(colours[3])
      t.up()
      for j in range(1,3):
        t.goto((x+(30*j)-600),-100)
        t.down()
        if(j==2):
          t.up()
          t.seth(0)
          t.fd(40)
          t.down()

        #Drawing vertical lines of Hashtag
        t.begin_fill()
        t.fd(40)
        t.lt(80)
        t.fd(200)
        t.seth(180)
        t.fd(40)
        t.lt(80)
        t.fd(200)
        t.end_fill()
        t.lt(100)

      #Drawing horizontal lines of hashtags
      for k in range(1,3):
        t.up()
        t.goto(x-600,(40*k)-100)
        t.down()
        if (k == 2):
          t.up()
          t.seth(90)
          t.fd(40)
          t.down()
          t.seth(0)

        #Drawing
        t.begin_fill()
        t.fd(200)
        t.lt(90)
        t.fd(40)
        t.lt(90)
        t.fd(200)
        t.lt(90)
        t.fd(40)
        t.end_fill()
        t.seth(0)

  #Calculation of total results
  total = slot1*slot2*slot3

  #Result output
  if (total == 1 or total == 8 or total == 27):
    print("YOU GOT A JACKPOT!!")
  else:
    print("You did not get anything")
    print("You are now at $"+str(money)+".")

  #How much money gained if won Jackpot
  if(total == 1):
    print("You have gotten 3 dollar signs in a row. You have gained $50")
    money = money + 70
    print("You are now at $"+str(money)+".")
  if(total == 8):
    print("You have gotten 3 7's in a row. You have gained $100")
    money = money + 120
    print("You are now at $"+str(money)+".")
  if(total == 27):
    print("You have gotten 3 hashtags in a row. You have gained $20")
    money = money + 40
    print("You are now at $"+str(money)+".")

  #Play again
  if(money > 10):
    replay2 = input("Would you like to play again? yes/no, Yes/No, YES/NO, y/n, Y/N.")
    if(replay2 == "yes" or replay2 == "Yes" or replay2 == "YES" or replay2 == "y" or replay2 == "Y"):
      t.clear()
      print("")

    elif(replay2 == "no" or replay2 == "No" or replay2 == "NO" or replay2 == "n" or replay2 == "N"):
      replay = False

    else: 
      print("Error! That is not one of the answer options given.")
      while(replay2 != "Yes" and replay2 != "yes" and replay2 != "YES" and replay2 != "y" and replay2 != "Y" and replay2 != "No" and replay2 != "no" and replay2 != "NO" and replay2 != "n" and replay2 != "N"):
        replay2 = input("Would you like to play again? yes/no, Yes/No, YES/NO, y/n, Y/N.")

        if(replay2 == "yes" or replay2 == "Yes" or replay2 == "YES" or replay2 == "y" or replay2 == "Y"):
          t.clear()
          print("")

        elif(replay2 == "no" or replay2 == "No" or replay2 == "NO" or replay2 == "n" or replay2 == "N"):
          replay = False
        else: 
          print("Error! That is not one of the answer options given.")

#End
print("Thanks for playing the slot machine game, hope you enjoyed! You're leaving with $"+str(money)+". Goodbye!")