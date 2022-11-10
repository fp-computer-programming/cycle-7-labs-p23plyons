# Author: PCL 11/10/22

#creating 5 inputs for the user to give 5 different words
w1 = input("please input a random word: ")
w2 = input("please input different random word: ")
w3 = input("please input another different random word: ")
w4 = input("please input another different random word: ")
w5 = input("please input another different random word: ")

#putting the inputs into a list in the order they were given 
#and creating a list of the lengths of the inputs in the order they were given
words = [w1,w2,w3,w4,w5]
word_lengths = [len(w1),len(w2),len(w3),len(w4),len(w5)]
print(words)
print(word_lengths)


