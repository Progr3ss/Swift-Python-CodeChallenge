

def is_palindrome(s):
    return reverseString(s) == s

def reverseString(s):
    
    rev = ''
    for ch in s:
        rev = ch + rev

    return rev

def toString(l):
    return ''.join(l)

def permute(a,l,r):
    
    #a.replace(' ' '') 
    newA = []    
    if l == r:
        print(toString(a))
       # print(is_palindrome(a.replace(' ','')))
        #newString = toString(a).replace(' ','') 
        #print(newString)
        #print(is_palindrome(newString) == true)
       # print(toString(''))
        #if is_palindrome(newString) == True:
            
            #newA.append(newString)
           # print(is_palindrome(newString),"permutations :",toString(a))
            #return newA

    else: 
        for i in range(l,r+1):
               
            a[l],a[i] = a[i], a[l]
            permute(a,l+1,r)
            a[l],[i] = a[l],a[l]


    

a = '123'
#a = 'tact coa'
n = len(a)
a = list(a)

print(permute(a,0,n-1))
#print(is_palindrome('racecar'))
#print(reverseString("rac"))

