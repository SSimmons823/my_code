#!/usr/bin/env python3

#create a list of dog names(3)
doglist = ["Prince", "Lady", "Honey"]
print(doglist)

#creat a list of cat names(3)
catlist = ["Sassy", "Missy", "Queen"]

#Append the cats list onto the dogs list (so it is a single list)
doglist.append(catlist)
print(doglist)

#Print out the first dog name from your single list
print(doglist[0])

#Print out the second cat name from your single list
print(doglist[3][1])

#Create a dictionary with the keys "first_dog" and "second_cat"
#Use the appropriate values from your list as the values for the dictionary keys
catdog = {"first_dog": doglist[0], "second_cat":doglist[3][1]}

#Print out the dictionary
print(catdog)

#Print out the value of "first_dog" and "second_cat" from the dictionary
print(catdog['first_dog'], catdog['second_cat'])
