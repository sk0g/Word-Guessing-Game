# Safely try to open a file, and print an error message if unsuccessful
def FileOpen(name)
    try:
        f = open(name, 'r')
        return f
    except IOError:
        print("Error: File does not exist, or is not called " + name)
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
                print('Improper value. Expected input was between' + str(minimum) ' and ' + str(maximum))
        except ValueError:
            continue
    return a


f = FileOpen('dictionary.txt')
guesses = integer_in(1, 100, 'Please enter how many guesses the computer will be allowed: ')
