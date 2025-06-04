def summation(num):
#    numlist = []
#    for i in range(1, num + 1):
#        numlist.append(i)
#    sumlist = sum(numlist)
    numlist = [n for n in range(1, num + 1)]
    sumlist = sum(numlist)
    return sumlist

print(summation(8))

    
   
    
