def number(bus_stops):
    arr = bus_stops
    inside = []
    out = []
    for i in range(len(arr)):
        inside.append(arr[i][0])
        out.append(arr[i][1])  
    total = sum(inside) - sum(out)  
    return total
        

        

print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
