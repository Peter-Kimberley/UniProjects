# flash_card_python
# a flash card systme for python


from random import *

# setting up the glossary
glossary = {'word1': "definition1", 
            'word2':"definition2", 
            'word3': "definition3"}

# sets the flag variable to False
exit = False

# the flashcard function
def flashcard():
    """Show a falsh card to the user
    and ask for a definition"""
    random_key = choice(list(glossary))
    print("define", random_key)
    input("Press return to see the definition.")
    print(glossary[random_key])
    

while not exit:
    user_input = input("Press s to show flashcard or Q to quit.")
    if user_input == 'q':
         exit = True
    elif user_input == 's':
        flashcard()
    else:
        print("You need to enter either q, or s.")
            
        
       








