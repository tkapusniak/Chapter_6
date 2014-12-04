#improving Ask_Number() function
#Created by Tyler Kapusniak
#Created on 11/19/2014

def ask_number(question, low, high, step = 1):

 """Ask for a number within a range."""

 response = None

 while response not in range(low, high):

 response = int(input(question))

 return response
