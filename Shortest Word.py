def find_short(s):
    splitstr = s.split()
    def lengthWords(w):
        return len(w)
    return splitstr.sort(key=lengthWords)

print(find_short("bitcoin take over the world maybe who knows perhaps"))