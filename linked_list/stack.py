class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def append(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def pop(self):
        fast = self.head.next
        slow = self.head
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = None
        self.length -= 1
        
        return fast
                
stack = Stack()
stack.append(1)
stack.append(2)
stack.append(3)