"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

sentence = input("Enter your sentence: ")
x = sentence.split(" ")
print(len(x))