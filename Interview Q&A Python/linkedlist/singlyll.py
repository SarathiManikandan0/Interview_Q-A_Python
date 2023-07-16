
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def display(self):
        if self.head is None:
            print("linked list is Empty.")
        else:
            current = self.head
            while current:
                print(current.data, end = " ")
                current = current.next
            print()
            
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.display()

#The Node class represents a single node in the linked list. It has two attributes: data, which stores the data of the node, and next, which stores a reference to the next node in the list.
#The LinkedList class represents the linked list itself. It has a single attribute, head, which stores the reference to the first node in the list. The class provides two methods:

#append(data): This method appends a new node with the given data at the end of the linked list. If the list is empty, it sets the new node as the head. Otherwise, it traverses the list until it reaches the last node and adds the new node there.

#display(): This method displays the elements of the linked list. It starts from the head and traverses the list, printing the data of each node.

#In the test part of the code, we create an instance of the LinkedList class called my_list. We then use the append() method to add three nodes with data values 10, 20, and 30, respectively. Finally, we call the display() method to print the contents of the linked list.


