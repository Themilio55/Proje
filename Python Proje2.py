list = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(l):
    for i in l:
        i.reverse()
    l.reverse()
    return(l)

reverse_list(list)