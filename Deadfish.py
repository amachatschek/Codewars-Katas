def parse(data):
    result = []
    num = 0
    chars = [x for x in data]
    for i in chars:
        match i:
            case "i":       #increment
                num += 1    
            case "d":       #decrement
                num -= 1
            case "s":       #square
                num ** 2
            case "o":       #output
                result.append(num)
        print(f"{i}: {result}")
    return result 

parse('iiisxxxdoso')