class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        """
        Initialize a new linked list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    
    def print_list(self):
        """
        Print the linked list items.
        """
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        """
        Add an item to the end of the linked list.
        """
        new_node = Node(value)        
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        
        return True
        
    def prepend(self, value):
        """
        Add an item to the beginning of the linked list.
        """
        if self.head is None:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
        return True
    
    def get(self, index):
        """
        Get an item from the linked list.
        """
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            
        return temp
    
    def pop(self):
        """
        Remove and return the last item from the linked list.
        """  
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        while temp.next:
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp
    
    def pop_first(self):
        """
        Remove and return the first item from the linked list.
        """
        if self.length == 0:
            return None
        
        old_node = self.head
        self.head = self.head.next
        old_node.next = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
        
        return old_node
        

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.prepend(3)
print(my_linked_list.print_list())
