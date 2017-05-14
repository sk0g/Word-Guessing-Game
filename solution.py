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
    word_len = len(word_list[0])
    occurences_list = [0] * (word_len + 1)
    for word in word_list:
        num = word.find(guess_char)
        occurences_list[num] += 1
    most_common, highest_val = 0, 0
    for i in range(word_len + 1):  # Find the most common length
        if occurences_list[i] > highest_val:
            highest_val = occurences_list[i]
            most_common = i
    if most_common == word_len:
        most_common = -1
    return most_common


def get_biggest_category_wordlist(word_list, char, index):
    words = [word for word in word_list if word.find(char) == index]
    return words


def list_to_string(ls):
    return("".join(ls))


def game_process():
    word_lengths = get_word_lengths(word_list)
    guesses_num = int(input('How many guesses would you like?\n'))
    word_length = integer_in(word_lengths, "What should your word length be?")
    word_hint = eval(input('Do you want to see the running total of remaining valid guesses?\n1 for yes, 0 for no. '))
    valid_words = [word for word in word_list if len(word) == word_length]
    display_word = ["-"] * word_length

    guessed_chars = []
    used_words_list = []
    won = False
    while guesses_num:
        if won:
            break
        else:
            print("You have", guesses_num, "guesses remaining. \n \n")
        char_guess = char_in(used_words_list)
        guessed_chars.append(char_guess)
        used_words_list.append(char_guess)
        index = get_biggest_category_index(char_guess, valid_words)
        valid_words = get_biggest_category_wordlist(valid_words, char_guess, index)
        if 0 <= index < word_length:
            display_word[index] = char_guess
            print("The letter was found at position number: ", index + 1)
        else:
            print("The letter you guessed wasn't in the word.")
            print("One less guess for you then.")
            guesses_num -= 1
        print("You have guessed the following letters:", " ".join(guessed_chars))
        if word_hint:
            print("Number of words remaining:", len(valid_words))
        print(list_to_string(display_word))
        if "-" not in display_word:
            won = True
    if won:
        print("Well done, you found the word!")
        print(list_to_string(display_word))
    else:
        print("Well, you didn't win... Might as well show you the word.")
        print(choice(valid_words))


dictionary_file = file_open('dictionary.txt')
word_list = file_process(dictionary_file)
replay = True
while replay:
    game_process()
    replay = eval(input('Would you like to play another game\
                        \n1 for yes, 0 for no. '))


