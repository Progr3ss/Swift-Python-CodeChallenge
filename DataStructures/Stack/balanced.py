from Stacks import Stack
stack = Stack()

def balanceParen(s):
    
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    if len(s) % 2 != 0:
        return False 

    for paren in s: 
        if paren in opening:
            stack.push(paren)
        else:
            if stack.isEmpty():
                return False 
            else:
                last_open = stack.pop()

            if(last_open, paren) not in matches:
                return False 
    return stack.isEmpty() 


p = '{[]'
print(balanceParen(p))
