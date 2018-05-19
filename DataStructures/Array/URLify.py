
s = "Mr John Smith" 
def URLify(s):
    for i in s:
        if i == " ":
            return s.replace(i,"%20")

print(URLify(s))
