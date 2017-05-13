from numpy.random import choice


def file_open(name):
    try:
        f = open(name, "r")
        return f
    except IOError:
        print("Error:", name, "not found")
        return False


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
        if a <= 0 or a not in length_list:
            print('No word found for that length, try again.')
        else:
            return a


def char_in(used_words_list):
    while True:
        c = input('Please enter your next character:')
        if len(c) == 1 and 'A' <= c <= 'z' and c not in used_words_list:
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


def get_biggest_category_index(guess_char, word_list):
    word_len = len(word_list[0]) + 1
    occurences_list = [0] * word_len
    for word in word_list:
        num = word.find(guess_char)
        occurences_list[num] += 1
    most_common, highest_val = 0, 0
    for i in range(word_len):  # Find the most common length
        if occurences_list[i] > highest_val:
            highest_val = occurences_list[i]
            most_common = i
    if most_common == word_len - 1:
        most_common == -1
    return most_common


dictionary_file = file_open('dictionary.txt')
word_list = file_process(dictionary_file)
word_lengths = get_word_lengths(word_list)

guesses_num = int(input('How many guesses would you like?\n'))
replay = True
while replay:
    word_length = integer_in(word_lengths, "What should your word length be?")
    word_hint = eval(input('Do you want to see the running total of remaining valid guesses? \
                            1 for yes, 0 for no.\n'))
    valid_words = [word for word in word_list if len(word) == word_length]
    display_word = ["-"] * word_length

    guessed_chars = []
    used_words_list = []
    won = False
    while guesses_num:
        if won:
            break
        char_guess = char_in(used_words_list)
        guessed_chars.append(char_guess)
        used_words_list.append(char_guess)
        index = get_biggest_category_index(char_guess, valid_words)
        valid_words = [word for word in valid_words if word.find(guessed_chars) == index]
        if 0 <= index < word_length:
            display_word[index] = char_guess
            print("The letter was found at position number: ", index+1)
            print("Your current word is: "".join(display_word")
            print("You have guessed the following letters:", guessed_chars)
        else:
            print("The letter you guessed wasn't in the word.")
            print("One less guess for you then.")
            print('You have', guesses_num, 'guesses remaining.\n')
            guesses_num -= 1
        if word_hint:
            print(len(valid_words))
        if "-" not in display_word:
            won = True
    if won:
        print("Well done, you found the word!")
        print("".join(display_word))
    else:
        print("Well, you didn't win... Might as well show you the word.")
        print(choice(valid_words))

    replay = eval(input('Would you like to play another game\
                        1 for yes, 0 for no.\n'))
