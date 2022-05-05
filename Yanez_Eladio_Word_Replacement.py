# The first input we need.
string_user_input = input()
string_words_split = string_user_input.split()
# The second input we need.
string_sentence_input = input()
string_sentence_split = string_sentence_input.split()

# This establishes the length of the code, we will be using this in the next bit of code.
loop_START = 0
loop_STOP = len(string_words_split)
loop_STEP = 2
# The START is the index we start at, which is 0. The STOP is where the loop ends, we use the length for the stopping
# point. The STEP/STRIDE is the amount of index points skipped over, so in the phrase "I love that dang coffee,"
# "I" (0, the start,) "that" (2, 2 indexes away from "I"/0,) and "coffee" (4, 2 indexes away from "that"/2, and is the
# length of the code, thus it ends here.)
for i in range(loop_START, loop_STOP, loop_STEP):
    # This searches for thew word in the sentence.
    if string_words_split[i] in string_sentence_split:
        # This replaces the original word in the phrase with the new word, i is the initial word and i +1 is the new
        # word. If string_user_input = coffee water, and string_user_input is "I love coffee," the new phrase would be
        # "I love water."
        string_sentence_input = string_sentence_input.replace(string_words_split[i], string_words_split[i + 1])
print(string_sentence_input)
