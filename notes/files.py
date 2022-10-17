#Python 07 - Files B 

# fileHandle -> can be treated as a sequence of strings

#counting lines in a File

fhand = open('ntext.txt')
count = 0
for line in fhand:
    count = count + 1
    print("line Count :", count)


#You can remove white space from right side of a string using rStrip()

quit() # -> is usefull when you want to stop executing because we discover some type of error

continue #in the middle of the loop, skips to the next iteration of the loop 