

from Node import Node


def removeDup(l):
    un = set ()
    while l :
        x = l.value
        l = l.next
        un.add(x)
    return un
#o(n)
def removeDup2(l):
    
    currNode = l.next
    dic = {currNode.next: True}
    if(l.next != None):
        currNode = l.next

        #dic = {currNode.next: True}

        while currNode.next != None:
            
            if currNode.next.value in dic:
                currNode.next = currNode.next.next
                  
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next
               # a.append(currNode.value) 
    return dic


        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(3)
e = Node(2)

a.next = b
b.next = c
c.next = d
d.next = e
print(removeDup2(a))

#print(removeDup(a))

