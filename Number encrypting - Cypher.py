def cypher(s):
    nums = [str(x) for x in range(10)]
    ltrs = [("O", "o"), ("I", "l"), ("R", "z"), ("E", "e"), ("A", "a"), ("S", "s"), ("G", "b"), ("T", "t"), ("B",), ("g",)]
    transl = str.maketrans(zip(ltrs, nums))
    
    return s, transl


print(cypher("Hello World"))