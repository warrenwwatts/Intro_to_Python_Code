# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 08:44:11 2018
Exercises for chapter 8 - Lists
@author: warren watts
"""


# code for 8.2, 8.3
fhand = open('mbox-break.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
fhand.close()   
 

# Exercise 2: Figure out which line of the above program is 
# still not properly guarded. See if you can construct a text file 
# which causes the program to fail and then modify the program so 
# that the line is properly guarded and test it to make sure it 
# handles your new text file.

fhand = open('mbox-break.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) > 2:
        print(words[2])
print(fhand.closed)
fhand.close()
print(fhand.closed)


# Exercise 3: Rewrite the guardian code in the above example without two
# if statements. Instead, use a compound logical expression using the and 
# logical operator with a single if statement.
 
fhand = open('mbox-break.txt', 'r')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) > 2 and words[0] == 'From':
        print(words[2])
fhand.close()

# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. 
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. 
# If the word is not in the list, add it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.

word_list = []
with open('romeo.txt','r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word not in word_list:
                word_list.append(word)
word_list.sort()
print(word_list)

print(file.closed)




# Exercise 5: Write a program to read through the mail box data and when
# you find line that starts with "From", you will split the line into
# words using the split function. We are interested in who sent the
# message, which is the second word on the From line.

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) > 1 and words[0] == 'From':
        print(words[1])
        count += 1
fhand.close()
# print using formatting 
print("There were %d lines in the file with From as the first word" % count)

