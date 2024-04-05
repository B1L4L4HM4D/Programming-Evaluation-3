#-------------------------------------------------------------------------------------------#

#Generate a random number between 1 and 100 using the uniform() function from random. After generating this number, ask the user to choose the amount of decimal places that the random number will be rounded to. For example, if the user chooses 3, the rounded number would be 3.141. If they user chooses 1, the output would be 3.1.

import random
#imports random module
import math
#imports math module
random_number = random.uniform(1, 100)
#generates a random number between 1 and 100
print(random_number)
#prints the random number
decimal_places = int(input("Enter the number of decimal places to round to: "))
#asks the user to input the number of decimal places they want to round to
rounded_number = round(random_number, decimal_places)
#rounds the random number to the given number of decimal places
print("The rounded number is:", rounded_number)
#prints the rounded number

#------------------------------------------------------------------------------------------#

#Create a program that prompts the user to enter their first name. Using only a loop, count the amount of letters in their name. Ask for their last name, and count the letters in their last name. Output their special ID number which is the first letter amount and the second amount (NOT ADDED TOGETHER). For example: Connor=6, Rilett=6, ID=66

firstName = str(input("Enter your first name: "))
lastName = str(input("Enter your last name: "))
#asks the user to input their first and last name

def count_letters_first_name(firstName):
  count = 0
  for x in firstName:
    count += 1
  return str(count)
#a function that counts the number of letters in the first name

def count_letters_last_name(lastName):
  count = 0
  for x in lastName:
    count += 1
  return str(count)
#a function that counts the number of letters in the last name

specialID = count_letters_first_name(firstName) + count_letters_last_name(lastName)
#adds the number of letters in the first and last name together

print("Your special ID number is:", specialID)
#prints the special ID number

#------------------------------------------------------------------------------------------#
      
