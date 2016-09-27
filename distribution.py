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
import string
alphaList = list(string.ascii_lowercase)
intext = str(input("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "' + intext + '" is: ')
listtext = intext.lower()
numList = list(range(1,27))
list1 = []
list1.append(listtext.count('a'))
list1.append(listtext.count('b'))
list1.append(listtext.count('c'))
list1.append(listtext.count('d'))
list1.append(listtext.count('e'))
list1.append(listtext.count('f'))
list1.append(listtext.count('g'))
list1.append(listtext.count('h'))
list1.append(listtext.count('i'))
list1.append(listtext.count('j'))
list1.append(listtext.count('k'))
list1.append(listtext.count('l'))
list1.append(listtext.count('m'))
list1.append(listtext.count('n'))
list1.append(listtext.count('o'))
list1.append(listtext.count('p'))
list1.append(listtext.count('q'))
list1.append(listtext.count('r'))
list1.append(listtext.count('s'))
list1.append(listtext.count('t'))
list1.append(listtext.count('u'))
list1.append(listtext.count('v'))
list1.append(listtext.count('w'))
list1.append(listtext.count('x'))
list1.append(listtext.count('y'))
list1.append(listtext.count('z'))
num2list = numList[::-1]


kobinierteliste = zip(list1, num2list, alphaList)
kobinierteliste = list(kobinierteliste)
kobinierteliste.sort(reverse=True)
counter = 0
while counter < 26:
    if kobinierteliste[counter][0] != 0:
        print(str(kobinierteliste[counter][2])*int(kobinierteliste[counter][0]))
    counter += 1