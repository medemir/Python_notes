# import your data
file = open("data.txt", "rt")
# read data
data = file.read()
# split words
words = data.split()
# count and print
print('Number of words in text file :', len(words))