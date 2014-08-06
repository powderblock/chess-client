from __future__ import print_function
import sys
from colorama import *

#Init Colorama
init()

#Chessboard width and height
width, height = 8,8

letters = {"A","B","C","D","E","F","G","H"}
numbers = ['1','2','3','4','5','6','7','8',]

#Nested for loop for board handling
for x in range(0, width):
    for y in range(0, height):
        if y % 2 == 0:
            print(Fore.YELLOW+Back.WHITE+'-',end='')

        if y % 2 != 0:
            print(Fore.WHITE+Back.YELLOW+'-',end='')

    #Print numbers for the rows.
    print(Fore.WHITE+Back.BLACK+' '+numbers[x])
    print('\n')

#Print letters for the columns.
print("ABCDEFGH")
