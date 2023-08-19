# Starter file for TM112 2023D TMA03 Q2


"""
This flashcard program allows the user to ask for a word_list entry.
In response, the program randomly picks an entry from all word_list
entries. It shows the entry. After the user presses return, the
program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

# IMPORTANT
# Q2 (a)(iii) Make changes only to
# -- the docstring for the program as a whole;
# -- the docstring of the show_flashcard() function;
# -- the body of the show_flashcard() function.


def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(element_list))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(element_list[random_key])

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
