#6.PY
# Defi:-Write a program that takes the line of input discarding the punctuation.Now break the line into words by spaces and iterate through the line.And make a dictionary so that the key will be the "word" that is read from the line and value will be the frequency that how many times this work came into the line.Print that dictionry onto the screen.
fname = input('Enter The File Name:  ')
fname=open(fname)
fname=fname.read()
word_count=dict()
fsplit=fname.split()
for word in fsplit:
    word_count[word] = word_count.get(word,0)+1

print(word_count)