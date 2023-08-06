# flash_cards_for_Tm112_gloassary
# a flash card system in python

#Importing built in fuctions
from random import *
import csv


# the flashcard function
def flashcard():
    """Show a falsh card to the user
    and ask for a definition"""
    random_key = choice(list(glossary))
    print("define", random_key)
    input("Press return to see the definition.")
    print(glossary[random_key])

# function to import file to dictionary
def file_to_dictionary(filename):
    """This will be using a file
        and importing it to a dictionary
        to use with flash cards"""
    file = open(filename, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary

# setting up the glossary using an imported CSV file
glossary = file_to_dictionary("TM112_Glossary.txt")

# sets the flag variable to False
exit = False    

# running the interactive loop
while not exit:
    user_input = input("Press s to show flashcard or q to quit.")
    if user_input == 'q':
         exit = True
    elif user_input == 's':
        flashcard()
    else:
        print("You need to enter either q, or s.")
            
        
       








