def open_or_senior(data):
    result = []
    for a, h in data:
        if a >= 55 and h > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))