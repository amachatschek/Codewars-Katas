def number(lines):    
    return [f"{i}: {item}" for i, item in enumerate(lines, 1)] 

print(number(["a", "b", "c"]))