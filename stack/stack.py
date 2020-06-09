"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list  import LinkedList, Node

#Method 1

 

    
    
    def __len__(self):
        return self.size

    

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
    def __repr__(self):
        return f"{self.storage}"
         

    def __len__(self):
        length=len(self.storage)
        return length #self.size

    def push(self, value):
        self.value= value
        self.size += 1
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

s= Stack()
while True:
    print(‘push<value>’)
    print(‘pop’)
    print(‘quit’)
do= input(‘What would you like to do?’).split()
operation= do[0].strip().lower()
if operation== ‘push’:
s.push(int(do[1]))
elif operation== ‘pop’:
    if s.is_empty():
        print(‘Stack is empty’)
    else:
        print(‘Popped value:’, s.pop())
elif operation==’quit’:
break


#Method 2
 
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __repr__(self):
        return f"{self.storage}"
         

    def __len__(self):
        return self.size

    def push(self, value):
        self.value= value
        self.size += 1
        self.storage..add_to_tail(value)

    def pop(self):
        if self.size ==0:
            return None
        else:
            self.size-=1
            self.storage.tail
            return self.storage.remove_head()

