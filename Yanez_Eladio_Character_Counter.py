phrase = input()
# Rather than splitting the statement and creating complications, I thought it was easier to keep it as one string,
# having 0 as the letter avoids for words being in place. 
letter = phrase[0]
# Search helps define where to look for the letter.
search = phrase[1: ]
# Having 0 represent the letter is really helpful for the search and avoiding complications. 
amount = search.count(letter)
print(amount)
