


def oneAway(s1, s2):
    s1n = len(s1)
    s2n = len(s2)

    if abs(s1n - s2n) == 1:
        return True

    elif abs(s1n - s2n) == 0:
        if s1 == s2:
            return True
        else:
            return False       

s1 = 'pale'
s2 = 'ple'
print(oneAway(s1,s2))
   
