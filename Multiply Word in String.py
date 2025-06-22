def modify_multiply(st, loc, num):
    return str((st.split()[loc] + "-") * num).rstrip("-")


print(modify_multiply("Creativity is the process of having original ideas that have value. It is a process; it's not random.",8 ,10))