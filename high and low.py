def high_and_low(numbers):
    num_list = numbers.split(" ")
    list_int = [int(x) for x in num_list]
    num_max = max(list_int)
    num_min = min(list_int)
    return f"{num_max} {num_min}"

print(high_and_low("2 -2 5 -1 4"))



