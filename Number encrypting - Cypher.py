def cypher(s):
    nums = [str(x) for x in range(10)]
    ltrs = [("O", "o"), ("I", "l"), ("R", "z"), ("E", "e"), ("A", "a"), ("S", "s"), ("G", "b"), ("T", "t"), ("B", None), ("g", None)]
    table = str.maketrans(zip(ltrs, nums))
    transl = s.translate(table) 
    return transl


print(cypher("Hello World"))