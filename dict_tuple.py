# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:35:27 2018
Dictionary and Tuple code.
@author: warren Watts
"""
# A dictionary
fav_albums = {"Beatles" : "Abbey Road",
              "Rolling Stones": "Exile on Main Street",
              "Billy Bragg": "Worker's Playtime",
              "Parliment" : "Motor Booty Affair",
              "Van Morrison" : "Astral Weeks",
              "Kendrick Lamar" : "DAMN.",
              "Mitski" : "Bury My Heart at Makeout Creek",
              "Tyler the Creator" : "Flower Boy",
              "Tame Impala" : "Currents", 
              "The 1975" : "A Brief Inquiry into Online Relationships",
              "Public Enemy" : "It Takes a Nation of Millions to Hold Us Back",
              "Bob Marley" : "Exodus",
              "Green Day" : "American Idiot"}

print(fav_albums)
print()
print(type(fav_albums))
print()
print(fav_albums.keys())
print()
print(fav_albums.values())
print()

# iterating through a dictionary and getting tuple containing key and value
for pair in fav_albums.items():
    print(pair)
print()

# iterating through a dictionary and getting key and value
for key, value in fav_albums.items():
    print(key, "-", value)
print()

# sorting a dictionary by key
for key, value in sorted(fav_albums.items()):
    print(key,"-", value)

# sorting a dictionary by key in reverse order
for key, value in sorted(fav_albums.items(), reverse = True):
    print(key,"-", value)
     
# sorting a dictionary by value
# using a function as a argument      
def sec_item(x):
    return x[1]
    
for key, value in sorted(fav_albums.items(), key = sec_item):
    print(value,"-", key)
   
# using a lambda function    
for key, value in sorted(fav_albums.items(), key = lambda x: x[1]):
    print(value,"-", key)
    
    
# sets are a list of unique values
# create a set, list and a tuple from the same data
my_set = {1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 6}
my_list = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 6]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 6)

# print all 3
print("Set =", my_set)
print("List =", my_list)
print("Tuple =", my_tuple)

# add an item to all 3
my_set.add(9)
my_list.append(9)
my_tuple.append(9)


# print set and list
print("Set =", my_set)
print("List =", my_list)



# add a duplicate item to set and list
my_set.add(9)
my_list.append(9)

# print set and list
print("Set =", my_set)
print("List =", my_list)


# iterating through 2 lists with zip
insult1 = ["Your", "was", "hamster,", "your", "smelt", "elderberries."]
insult2 = ["mother", "a", "and", "father", "of", "<snark>"]

for pair in zip(insult1, insult2):
    print(pair)
    
for word1, word2 in zip(insult1, insult2):
    print(word1, word2, end =" ")

