







def simplify(list):
    list.append(999999999)
    newList = []

    i = 0
    while(i<len(list)-1):
        p = 0
        start = list[i]
        while(list[i]+1 == list[i+1]):
            p+=1
            i+=1
        if(p > 0):
            strGroup = str(start)+ "-" +str(p)
        else:
            strGroup = start

        newList.append(strGroup)
        i+=1
    return newList


# [0,1,4,5,6,7,8,11,12,14]
# [0-1,4-4,11-1,14]