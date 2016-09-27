"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>
        https://github.com/TheBigBlueBlob/Character-Distribution/blob/master/distribution.py
Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
uselessvariable = 0
import string
alphaList = list(string.ascii_lowercase)
origText = str(input("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "' + origText + '" is: ')
newOrigList = origText.lower()
numList = list(range(1,27))
MyList = []
MyList.append(newOrigList.count('a'))
MyList.append(newOrigList.count('b'))
MyList.append(newOrigList.count('c'))
MyList.append(newOrigList.count('d'))
MyList.append(newOrigList.count('e'))
MyList.append(newOrigList.count('f'))
MyList.append(newOrigList.count('g'))
MyList.append(newOrigList.count('h'))
MyList.append(newOrigList.count('i'))
MyList.append(newOrigList.count('j'))
MyList.append(newOrigList.count('k'))
MyList.append(newOrigList.count('l'))
MyList.append(newOrigList.count('m'))
MyList.append(newOrigList.count('n'))
MyList.append(newOrigList.count('o'))
MyList.append(newOrigList.count('p'))
MyList.append(newOrigList.count('q'))
MyList.append(newOrigList.count('r'))
MyList.append(newOrigList.count('s'))
MyList.append(newOrigList.count('t'))
MyList.append(newOrigList.count('u'))
MyList.append(newOrigList.count('v'))
MyList.append(newOrigList.count('w'))
MyList.append(newOrigList.count('x'))
MyList.append(newOrigList.count('y'))
MyList.append(newOrigList.count('z'))
NewnumList = numList[::-1]


tupleList = zip(MyList, NewnumList, alphaList)
tupleList = list(tupleList)
tupleList.sort(reverse=True)
counter = 0
while counter < 26:
    if tupleList[counter][0] != 0:
        print(str(tupleList[counter][2])*int(tupleList[counter][0]))
    else:
        uselessvariable += 1
    counter += 1