# Coding Trail 2
print ("Welcome to the Coding Trail. You will need to gather supplies, choose your route, and manage your resources as you travel. Each decision you make will affect your progress. Prepare yourself for challenges along the way. Good luck on your journey")
import random 
from random import randint
health = 100
food = 10
miles = 0
game = True
while game:
  Bear = randint (1,3)
  print ("Game Choice Options")
  print ("A. Eat food for health")
  print ("B. Fast pace")
  print ("C. Slow pace")
  print ("D. Stop for the night")
  print ("E. Status check") 
  print ("F. Steady pace")
  print ("G. Quit")
  choice = input("what is your choice?")
  if choice == "A":
    health = health + 10 
    food = food - 1
    print ("your health is now", health)
    print ("your food is now", food)
  elif choice == "B":
    health = health - 5
    miles = miles + randint(5,15)
    print ("your health is now", health)
    print ("you have now moved", miles, "miles")
  elif choice == "C":
    health = health - 2
    miles = miles + randint(3,4)
    print ("your health is now", health)
    print ("you have now moved", miles, "miles")
  elif choice == "D":
    miles = miles + 0
    health = health + randint(9,15)
    print ("your health is now", health)
    print ("you have now moved", miles, "miles")
  elif choice == "E":
    print ("your health is now", health)
    print ("you have moved a total of", miles, "miles")
  elif choice == "F":
    health = health - 3
    miles = miles + 6
    miles = miles + randint(3,8)
    print ("your health is now", health)
    print ("you have now moved", miles, "miles")
  elif choice == "G":
    game = False
  if Bear== 2:
    health= health - 10
    print ("Suddenly,a bear appears in front of you. You have to either fight. You lose 10 health points")
    

  if miles> 125:
    print ("you win")
    game = False  

  if health < 0:
    print ("you lose")
    game = False  