def is_opposite(s1,s2):
    opp1 = s1.swapcase()
    if s2 == opp1:
        return True
    elif s1 == "" and s2 == "":
        return False
    else:
        return False