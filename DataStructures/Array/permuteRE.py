

def toString(sList):
    return ''.join(sList)

def permuteStr(s):

    n = len(s)
    a = list(s)
    l = 0 
    r = n-1

    if l == r:
        print(toString(a))

    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permuteStr(s)
            a[l],a[i] = a[l],a[l]


print(permuteStr("123"))
