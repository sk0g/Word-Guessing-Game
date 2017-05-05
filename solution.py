# Safely try to open a file, and print an error message if unsuccessful
def FileOpen(name):
    try:
        f = open(name, 'r')
        return f
    except IOError:
        print("Error: File does not exist, or is not called " + name)
        return 0


def integer_in(length_list, statement):
    while True:
        print(statement)
        try:
            a = int(input())
        except ValueError:
            print('Improper number, try again.')
        if len(a) <= 0 or len(a) not in length_list:
            print('No word found for that length, try again.')
        else:
            return a


def generate_len_list(f):
    length_list = []
    for word in f:
        f_length = len(f)
        if f_length not in length_list:
            length_list.append(f_length)
    return length_list


f = FileOpen('dictionary.txt')
length_list = generate_len_list(f)

replay = True
while replay:
    word_length = integer_in(length_list, "What should your word length be?")
    word_hint = eval(input('Do you want to see the running total of remaining valid guesses?\
                            1 for yes, 0 for no.'))
    valid_words = [word for word in f if len(word) == word_length]

    replay = eval(input('Would you like to play another game\
                        1 for yes, 0 for no.'))
