def file_open(name):
    try:
        f = open(name, 'r')
        return f
    except IOError:
        print("Error: " + name + " not found")
        return 0


def file_process(f):
    word_list = []
    for word in f:
        word.strip()
        if not word_has_dupes(word):
            word_list.append(word)
    return word_list


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


def char_in():
    while True:
        c = input('Please enter your next character:')
        if len(c) == 1 and 'A' <= c <= 'z':
            return(c.lower())
        else:
            continue


def word_has_dupes(word):
    lgt = len(word)
    for i in range(lgt-1):
        c = word[i]
        for j in range(i+1, lgt):
            if word[j] == c:
                return True
    return False


def get_word_lengths(word_list):
    length_list = []
    for word in word_list:
        word_length = len(word)
        if word_length not in length_list:
            length_list.append(word_length)
    return length_list


def get_biggest_category(guess_char, word_list):
    pass


dictionary_file = file_open('dictionary.txt')
word_list = file_process(dictionary_file)
word_lengths = get_word_lengths(word_list)

guesses_num = int(input('How many guesses would you like?'))
replay = True
while replay:
    word_length = integer_in(word_lengths, "What should your word length be?")
    word_hint = eval(input('Do you want to see the running total of remaining valid guesses?\
                            1 for yes, 0 for no.'))
    valid_words = [word for word in word_list if len(word) == word_length]
    for i in range(guesses_num):
        char_guess = char_in()

        print('You have', guesses_num - i, 'guesses remaining.\n')
        if word_hint:
            pass
            # print valid guesses left

    replay = eval(input('Would you like to play another game\
                        1 for yes, 0 for no.'))
