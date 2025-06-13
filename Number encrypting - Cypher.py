def cypher(s):
    nums = [str(x) for x in range(10)]
    ltrs = {"O", "o" ("I", "l"), ("R", "z"), ("E", "e"), ("A", "a"), ("S", "s"), ("G", "b"), ("T", "t"), ("B",), ("g",)}
    for i in ltrs:  
        a, b = i

    #transl = s.translate(table) 
    transl = dict.fromkeys(ltrs, nums)
    print(ltrs)
    return ltrs


print(cypher("Hello World"))