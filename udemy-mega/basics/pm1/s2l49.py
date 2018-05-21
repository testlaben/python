# open file, print each line's word's length

from __future__ import print_function

myfile = open("fruits.txt")
content = myfile.read()
content = content.splitlines()
myfile.close()
for i in content:
    print(len(i))
