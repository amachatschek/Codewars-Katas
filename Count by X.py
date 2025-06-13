def count_by(x, n):
    """
    Return an array of the first n multiples of x
    """
    new_list = []
    for i in range(n):
        new_list.append((i + 1) * x)
    return new_list
    
print(count_by(50, 5))