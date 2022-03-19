# lesson 18: data structures (udemy)
# comes in at a merciful 11 minutes
# pages 112 - 117 or so

# lists/dictionaries can be used for structured data

cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'} # create dictionary
allCats = [] # blank list
allCats.append( {'name': 'Zophie', 'age': 7, 'color': 'gray'}  )
allCats.append( {'name': 'Pooka', 'age': 5, 'color': 'black'}  )
allCats.append( {'name': 'fat-tail', 'age': 5, 'color': 'black'}  )
allCats.append( {'name': '???', 'age': 0, 'color': 'orange'}  )

# list of dictionaries = data structures

# dictionary stored example
# tic tac toe example

import pprint
# basic dictionary in python
# the strings used for keys like top-L notation is arbitrary
# 
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'middle-L': ' ', 'middle-M': ' ', 'middle-R': ' ',
            'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}


# output of above:
#{'bottom-L': ' ',
 #'bottom-M': ' ',
 #'bottom-R': ' ',
 #'middle-L': ' ',
 #'middle-M': ' ',
 #'middle-R': ' ',
 #'top-L': ' ',
 #'top-M': ' ',
 #'top-R': ' '}

 # change middle to X
 # 
#theBoard['mid-M'] = 'X'

#pprint.pprint(theBoard)

# formatting to look like tic tac toe board

# fucntion
# print functions

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
    print('-----')
    print(board['middle-L'] + '|' + board['middle-M'] + '|' + board['middle-R'] )
    print('-----')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'] )

#theBoard['middle-M'] = 'X' # set an arbitrary position

printBoard(theBoard)

# the type function
type(32)
# oputputs in
type(3.14)
# float
type(theboard[top-R])
#a string

