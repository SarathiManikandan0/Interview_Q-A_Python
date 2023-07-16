class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str,elements)))
        
    def display_backward(self):
        elements = []
        current = self.head
        while current.next:
            current = current.next
        while current:
            elements.append(current.data)
            current = current.prev
        print(" -> ".join(map(str, elements)))
        
# Test the doubly linked list implementation
if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.display_forward()
    linked_list.display_backward()
            
#Explanation:
#Node class: This class represents a node in the doubly linked list. Each node contains three attributes - data to store the value, prev to store the reference to the previous node, and next to store the reference to the next node.

#DoublyLinkedList class: This class represents the doubly linked list itself. It has a single attribute head, which is a reference to the first node in the doubly linked list.
#append method: This method is used to add a new node with the given data to the end of the doubly linked list. If the doubly linked list is empty (i.e., self.head is None), the new node becomes the head. Otherwise, it iterates through the doubly linked list using a while loop to find the last node. Then, it appends the new node to the next attribute of the last node and updates the prev attribute of the new node.
#display_forward method: This method is used to print the elements of the doubly linked list in the forward order. It iterates through the doubly linked list using a while loop, and for each node, it appends the data to a list called elements. Finally, it uses the join method to print the elements of the list separated by "->".
#display_backward method: This method is used to print the elements of the doubly linked list in the backward order. It first finds the last node of the doubly linked list by iterating from the head using a while loop. Then, it iterates backward through the doubly linked list using a while loop, starting from the last node. For each node, it appends the data to the elements list. Finally, it uses the join method to print the elements of the list separated by "->".
#In the test section, we create an instance of the DoublyLinkedList class called linked_list. We then use the append method to add three elements to the doubly linked list (1, 2, and 3). Finally, we call the display_forward and display_backward methods to print the doubly linked list in both forward and backward orders.

