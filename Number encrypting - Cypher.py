def cypher(s):
    nums = [x for x in range(10)]
    ltrs = [("O", "o"), ("I", "l"), ("R", "z"), ("E", "e"), ("A", "a"), ("S", "s"), ("G", "b"), ("T", "t"), ("B",), ("g",)]
    transl = dict(zip(ltrs, nums))
    for o, l in ltrs.items():
        

print(cypher("Hello World"))