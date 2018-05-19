

def stringRotation(s1,s2):
    
    if len(s1) != len(s2):
        return False

    double1 = s1 + s1

    return is_SubString(double1,s2)

def is_SubString(s1, s2): 

    return s1.find(s2) > -1
a = 'waterbottle'
b = 'erbottlewat'
print(stringRotation("waterbottle","erbottlewat"))
