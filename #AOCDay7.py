#AOCDay7
import re

f = [male.strip() for male in open("AOCDay7.txt" , "r")]


"""
cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
"""
total = 100000
#consider using a tree????
#start of a directory begins with $cd xyz and ends with $ls xyz or dir
# lines = [x.split('\n') for x in f]

input = ["cd /" , 'cd a', 'cd b', 'cd ..', 'cd c', 'cd d', 'cd ..', 'cd ..', 'cd ..', 'cd e']
#pop last element?

def directive(inp):
    director = []
    for put in inp:
        cdStarts = put.split(" ")
        if (cdStarts[1] == ".."):
            director.pop()
        else:
            director.append(cdStarts[1])
        print(director)


def elLadder(num):
    this = 0
    for m in num:
        if (isinstance(m,list)):
            this += elLadder(m)
        else:
            this += m
    return this


#if put != put+1, add to a separate list?       