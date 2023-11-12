#program to remove white spaces from a text list and 
#return a clean txt file w/ one word per new line.

def pagereader(pagelist_of_terms):
    f = open(pagelist_of_terms, "r")
    adj = f.read()
    f.close()

#pagereader("adjective_list.txt")

def pagemaker():
    adj = adj.title()
    adj_list = adj.split()
    #print(adj_list)
    #print line for troubleshooting steps only

    adj_set = set(adj_list)
    #print(adj_set)
    #print line for troubleshooting steps only

    adj_list = sorted(adj_set)
    #print(adj_list)
    #print('\n'.join(adj_list))
    #print line for troubleshooting steps only


def pagewriter(pagelist_of_terms):
    f = open(pagelist_of_terms, "w")
    f.write('\n'.join(adj_list))
    f.write('\n')
    f.close()

pagereader("adjective_list.txt")
pagemaker()
pagewriter("a_list.txt")

pagereader("animal_list.txt")
pagemaker()
pagewriter("b_list.txt")