


def twoSum(num, target):
    myDict = {}
    indexlist = []

    for (i,v) in enumerate(num):
        compliment = target - v
        print(compliment)
        if compliment not in myDict:
            myDict[v] = i
            #print(myDict)
        else:

            #print('my',myDict[compliment], 'com', compliment)
            indexlist.extend([i, myDict[compliment]])
            
    return indexlist

a = [2, 7, 11, 15]
print(twoSum(a,9))
