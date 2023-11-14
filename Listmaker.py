#program removes white spaces from a page of text and 
#return a clean txt file w/ one word per new line.

import os

def pagereader(page_name):
    f = open(page_name, "r")
    global adj
    adj = f.read()
    f.close()

def pagewriter(page_name):
    f = open(page_name, "w")
    f.write('\n'.join(adj_list))
    f.write('\n')
    f.close()

page_name = input("File name to be converted into a clean list?: ")
try:
    if os.stat(page_name).st_size>0:
        print("All good.  Cleaning list: {}".format(page_name))
except OSError:
    print("File not found: {}".format(page_name))
    exit()

pagereader(page_name)

#takes string from pagereader, capitalizes each word, splits words into list
adj = adj.title()
adj_list = adj.split()
print(adj_list)
#print line for t/s
#converting the list to a set eliminates duplicates
adj_set = set(adj_list)
print(adj_set)
#print line for t/s
#make a new sorted list from the set, and convert to a string w/ one word per new line
adj_list = sorted(adj_set)
print(adj_list)
print('\n'.join(adj_list))
#print line for t/s

pagewriter(page_name)
