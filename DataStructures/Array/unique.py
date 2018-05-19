


def unique(s):
    '''
    (str) -> bool
    return true or false if the string has duplicates
    '''
    return len(set(s)) == len(s)

def unique2(s):
    '''
     (str) -> bool
     return true or false if the string has duplicates.
    '''
    for ch in s:
        if s.count(ch) > 1:
            return False
    else:
        return True 



