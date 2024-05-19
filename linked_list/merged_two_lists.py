from linked_list import LinkedList

def mergeTwoLists(list1, list2):
        head = ListNode()
        temp = head

        while list1 and list2:
            if list1.value <= list2.value:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
                
            temp = temp.next
        
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return head.next


list1 = LinkedList()
list2 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(4)
list2.append(1)
list2.append(3)
list2.append(4)

print(mergeTwoLists(list1, list2))