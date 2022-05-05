# This asks for the user to type out a sentence, this is merely for clarity sake.
print('Please type out a sentence.')
# Defines the user input.
string_phrase = input()
# Creates the split necessary for words.
string_split = string_phrase.split()
# This is the empty dictionary we fill out.
word_count = {}
# We use the inputs the user in as a basis to put into the dictionary.
for i in string_split:
    if i in word_count:
        # This implies the word being seen.
        word_count[i] = word_count[i] + 1
    else:
        # This implies the word is new.
        word_count[i] = 1
# We use i in string_split as the loop so this statement repeats for about as many times as how unique a word is within
# a phrase. i itself stands for the word used, while word_count[i] is the value/amount of times the unique word has been
# used.
for i in string_split:
    if i in word_count:
        print(i, word_count[i])