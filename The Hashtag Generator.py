def generate_hashtag(s):
    wordlist = (s.strip()).split()
    tag = "#"
    for w in wordlist:
        tag += w.capitalize()
    return tag

print(generate_hashtag('Codewars      '))
print(generate_hashtag('codewars  is  nice'))