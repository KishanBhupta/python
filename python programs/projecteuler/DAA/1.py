class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def count_last_element_occurrences(self):
        if not self.head:
            return 0
        
        last_element = self.head
        while last_element.next:
            last_element = last_element.next
        
        count = 0
        current = self.head
        while current:
            if current.value == last_element.value:
                count += 1
            current = current.next
        
        return count

# Example usage
linked_list = LinkedList()
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(3)
linked_list.append(7)
linked_list.append(7)

count = linked_list.count_last_element_occurrences()
print("Number of occurrences of the last element:", count)
