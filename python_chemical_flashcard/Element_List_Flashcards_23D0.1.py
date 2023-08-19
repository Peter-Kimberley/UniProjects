# Starter file for TM112 2023D TMA03 Q2


"""
This program tests a users knowledge of chemical symbols.
The program asks the user to press the s key to show a flash card or press the q key to quit.
If the s key is pressed, the program randomly picks an chemical element from the element_list, 
and shows the element to the user, and then asks the user to type the correct chemical symbol,
if the user correctly types the symbol the user is informed that they are correct and the element
is removed from the element_list.
If the user gets the symbol wrong, the program then tells the user they are wrong and the correct symbol is shown. 
If correct the entry is removed from the element_list.
The program will eventually terminate once all chemical symbols have been
identified, and the element_list becomes empty.
"""

from random import *

# IMPORTANT
# Q2 (a)(iii) Make changes only to
# -- the docstring for the program as a whole;
# -- the docstring of the show_flashcard() function;
# -- the body of the show_flashcard() function.


def show_flashcard():
    """ ask the user what the symbol is
    for the shown element.    
    """
    random_key = choice(list(element_list))
    print('What is the symbol for ', random_key)
    answer = input('please enter the correct symbol: ')
    if answer == element_list[random_key]:
        print ('Well done you answered correctly')
        del element_list[random_key]
    else:
        print('The correct answer is'(element_list[random_key]))



## Set up the element_list
element_list = {'Sodium':'Na',
                'Potassium':'K',
                'Iron':'Fe',
                'Copper':'Cu',
                'Silver':'Ag',
                'Tin':'Sn',
                'Antimony':'Sb',
                'Tungsten':'W',
                'Gold':'Au',
                'Mercury':'Hg',
                'Lead':'Pb'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q' or len(element_list) == 0:
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')              
