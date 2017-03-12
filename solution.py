# Import spam
import random

# Safely try to open a file, and print an error message if unsuccessful
def file_open(name):
    try:
        f = open(name, 'r')
        return f
    except IOError:
        print("Error: File does not exist, or is not called " + name)
        return 0

# Bully user into answering with a "yes" or "no"
def prompt_looper(a, b = "yes", c = "no"):
    while 1:
        res = input()
        try:
            res = res.lower()
        except:
            print('Please type in one of either ' + b + ' or ' + c)
            continue
        if res == b:
            return True
        elif res == c:
            return False

# Safely read an integer, and discard inputs outside the specified range, or of other data types
def integer_in(minimum, maximum, statement = ''):
    a = minimum - 1
    # While loop keeps asking for another input if the input is not appropriate
    while a < minimum:
        try:
            print(statement)
            a = int(input())
            if a < minimum or a > maximum:
                print('Improper value. Expected input was between' + str(minimum) + ' and ' + str(maximum))
        except ValueError:
            continue
    return a

def play_game():
    guesses_num = integer_in(1, 100, 'Please enter how many guesses the computer should be allowed: ')
    print('The computer will be allowed to have ' + str(guesses_num) + ' guesses.')
    running_total_flag = prompt_looper("Do you want to have a running total of the remaining words?")

WORDS_LIST = []
WORDS_LIST_FILE = file_open('dictionary.txt')
# Add all words to a list for easier access
# Don't remove strip, or it will save the newlines to the list
for word in WORDS_LIST_FILE:
    WORDS_LIST.append(word.strip())
