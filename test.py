#program to remove white spaces from a text list and 
#return a clean txt file w/ one word per new line.


def pagereader(page_name):
    f = open(page_name, "r")
    global adj
    adj = f.read()
    f.close()

pagereader("test_list.txt")

adj = adj.title()
adj_list = adj.split()
print(adj_list)
#print line for t/s

adj_set = set(adj_list)
print(adj_set)
#print line for t/s

adj_list = sorted(adj_set)
print(adj_list)
print('\n'.join(adj_list))
#print line for t/s


def pagewriter(page_name):
    f = open(page_name, "w")
    f.write('\n'.join(adj_list))
    f.write('\n')
    f.close()

pagewriter("test_list.txt")
