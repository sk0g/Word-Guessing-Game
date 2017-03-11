Read the file dictionary.txt, which contains the full contents of the Official Scrabble
Player's Dictionary, Second Edition. This word list has over 120,000 words, which
should be more than enough for our purposes.


1. Prompt the user for a word length, re-prompting as necessary until they enter a
number such that there's at least one word that's exactly that long. That is, if the user
wants to play with words of length -42 or 137, since no English words are that long,
you should re-prompt them.

2. Prompt the user for a number of guesses, which must be an integer greater than zero.
Don't worry about unusually large numbers of guesses – after all, having more than
26 guesses is clearly not going to help your opponent!

3. Prompt the user for whether they want to have a running total of the number of words
remaining in the word list. This completely ruins the illusion of a fair game that you'll
be cultivating, but it's quite useful for testing

4. Play the Word Guessing game as described below:
    1. Construct a list of all words in the English language whose length matches the
    input length.

    2. Print out how many guesses the user has remaining, along with any letters the
    player has guessed and the current blanked-out version of the word. If the user
    chose earlier to see the number of words remaining, print that out too.

    3. Prompt the user for a single letter guess, re-prompting until the user enters a letter
    that she hasn't guessed yet. Make sure that the input is exactly one character long
    and that it's a letter of the alphabet.

    4. Partition the words in the dictionary into groups by word category.

    5. Choose a word category and remove all words from the word list that aren't in
    that category, and report the position of the letters (if any) to the user. If the word
    category doesn't contain any copies of the letter, subtract a remaining guess from
    the user.

    6. If the player has run out of guesses, pick a word from the word list and display it
    as the word that the computer initially “chose.”

    7. If the player correctly guesses the word, congratulate them.

    8. Ask if the user wants to play again and loop accordingly.
