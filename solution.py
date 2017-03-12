# Import spam
import random

# Safely try to open a file, and print an error message if unsuccessful
def FileOpen(name):
    try:
        f = open(name, 'r')
        return f
    except IOError:
        print("Error: " + name + " not found")
        return 0

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

words = []
f = FileOpen('dictionary.txt')
guesses_num = integer_in(1, 100, 'Please enter how many guesses the computer should be allowed: ')
print('The computer will be allowed to have ' + str(guesses_num) + ' guesses.')

# Add all words to a list for easier access
# Don't remove strip, or it will save the newlines to the list
for word in f:
    words.append(word.strip())
