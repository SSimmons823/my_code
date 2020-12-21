#!/usr/bin/env python3
"""ASCII Art Album || Author: Shameka Simmons"""

response = int(input("What ASCII art would you like to view? Please enter a number from the menu provided: "
                     "\n 1-Mermaid  2-Dog  3-Cat  4-Snake  5-Lion "
                     "\n Enter number: "))

Mermaid = 1
Dog = 2
Cat = 3
Snake = 4
Lion = 5

message = 'You chose to view '

if response == 1:
    message = message + 'Mermaid.'
    file = open("mermaid.txt", "r")
    print(message)
    print(file.read())
    file.close()

if response == 2:
    message = message + 'Dog.'
    file = open("dog.txt", "r")
    print(message + 'Dog.')
    print(file.read())

if response == 3:
    message = message + 'Cat.'
    file = open("cat.txt", "r")
    print(message + 'Cat.')
    print(file.read())

if response == 4:
    message = message + 'Snake.'
    file = open("snake.txt", "r")
    print(message)
    print(file.read())

if response == 5:
    message = message + 'Lion.'
    file = open("lion.txt", "r")
    print(message)
    print(file.read())

ask = input("Would you like to view more art? yes/no:")

yes = int(input("What ASCII art would you like to view? Please enter a number from the menu provided: "
                "\n 1-Mermaid  2-Dog  3-Cat  4-Snake  5-Lion "
                "\n Enter number: "))

no = quit("Have a great Day!!!")

print(ask)

if ask == yes:
    print(yes)

if ask == no:
    print()

