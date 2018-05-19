

def duplicateChar(s):
    return len(set(s)) == len(s)

s = 'abcde'
print(duplicateChar(s))
