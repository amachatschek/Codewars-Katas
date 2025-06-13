def filter_list(l):
    'return a new list with the strings filtered out'
    lc = [x for x in l if type(x) == int]
    return lc


print(filter_list([1,'a','b',0,15])) # == [1,0,15]