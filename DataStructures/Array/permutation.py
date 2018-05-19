

def toString(List):
    return ''.join(List)

def permute(a,l,r):
   
    if l == r:
            
        print(toString(a))
         #b = toString(a)

    else:
        for i in range(l,r+1):

            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l],[i] = a[l],a[l]


string = 'abc'
n = len(string)
a = list(string)
permute(a,0,n-1)

