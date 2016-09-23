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
string = str(input("Please enter a string of text (the bigger the better):"))
print('The distribution of characters in "{0}" is:'.format(string))
stringl = string.lower()
stringw = stringl.replace(" ", "")
stringp = stringw.replace(".", "")
lisstr = stringp
countr = len(lisstr)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
while countr > -1:
    countr -= 1
    if lisstr[countr] == 'a':
        a += 1
    elif lisstr[countr] == 'b':
        b += 1
    elif lisstr[countr] == 'c':
        c += 1
    elif lisstr[countr] == 'd':
        d += 1
    elif lisstr[countr] == 'e':
        e += 1
    elif lisstr[countr] == 'f':
        f += 1
    elif lisstr[countr] == 'g':
        g += 1
    elif lisstr[countr] == 'h':
        h += 1
    elif lisstr[countr] == 'i':
        i += 1
    elif lisstr[countr] == 'j':
        j += 1
    elif lisstr[countr] == 'k':
        k += 1
    elif lisstr[countr] == 'l':
        l += 1
    elif lisstr[countr] == 'm':
        m += 1
    elif lisstr[countr] == 'n':
        n += 1
    elif lisstr[countr] == 'o':
        o += 1
    elif lisstr[countr] == 'p':
        p += 1
    elif lisstr[countr] == 'q':
        q += 1
    elif lisstr[countr] == 'r':
        r += 1
    elif lisstr[countr] == 's':
        s += 1
    elif lisstr[countr] == 't':
        t += 1
    elif lisstr[countr] == 'u':
        u += 1
    elif lisstr[countr] == 'v':
        v += 1
    elif lisstr[countr] == 'w':
        w += 1
    elif lisstr[countr] == 'x':
        x += 1
    elif lisstr[countr] == 'y':
        y += 1
    elif lisstr[countr] == 'z':
        z += 1
print("a"*a)
