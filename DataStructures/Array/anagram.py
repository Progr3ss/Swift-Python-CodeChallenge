
def Anagram(s1,s2):
    return sorted(s1) == sorted(s2)

#s1 = 'clint eastwood'.replace(' ', '')
#s2 = 'old west action'.replace(' ', '')


def Anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
   
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1


    for k in count:
        if count[k] == 0:
            return False
    return True



s1 = 'clint eastwoadsod'.replace(' ', '')
s2 = 'old west actiadsn'.replace(' ', '')
print(Anagram(s1,s2))     

#print(Anagram(s1,s2))
