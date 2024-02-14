input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten_list = []

def flatten(l):
    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            flatten_list.append(i)
    return flatten_list


flatten(input_list)
