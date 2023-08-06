# flash_card_python
# a flash card systme for python


from random import *

# setting up the glossary
glossary = {'word1': "definition1", 
            'word2':"definition2", 
            'word3': "definition3"}

# the flashcard function
def flashcard():
    """Show a falsh card to the user
    and ask for a definition"""
    random_key = choice(list(glossary))
    print("define", random_key)
    








