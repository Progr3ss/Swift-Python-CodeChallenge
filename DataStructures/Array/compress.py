

def compressString(s):
    r = ""
    l = len(s)
    
    if l == 0:
        return ""

    last = s[0]
    cnt = 1
    i  = 1 
    print(s)
    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)
    return r
s = "aabcccfff"
print(compressString(s))
