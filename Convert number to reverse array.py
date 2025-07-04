def digitize(n):
    nlist = [i for i in str(n)].sort(reverse=True)
    print(nlist)
    return nlist

digitize(35231)