def number(lines):
    new_list = [f"{i}: {item}" for i, item in enumerate(lines, 1)]
    #for i, item in enumerate(lines, 1):
    #    new_list.append(f"{i}: {item}")    
    return new_list

print(number(["a", "b", "c"]))