# write the function is_anagram
def is_anagram(test, original):
    test_letters = []
    orig_letters = []
    for i in test:
        test_letters.append(i)
    for o in original:
        orig_letters.append(o)
    if test_letters < orig_letters:
        return True
    else:
        return False 

print(is_anagram("dumble", "bumble"))
print(is_anagram("bored", "robed"))