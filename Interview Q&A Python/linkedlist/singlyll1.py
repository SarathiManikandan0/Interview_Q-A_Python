
#Problem:
#Given a singly linked list, write a function to determine if the list has a cycle (i.e., there is a loop in the list). Return True if a cycle exists, and False otherwise.

#Example:
#Input: 1 -> 2 -> 3 -> 4 -> 2 (the list forms a cycle)
#Output: True

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False
#Test the Function
if __name__ == '__main__':
    #create a cycle linked list
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    
    has_cycle_result = has_cycle(head)
    print(has_cycle_result)
    
#Node class: Same as before, this class represents a node in the linked list.

#has_cycle function: This function takes the head of the linked list as input and checks if there is a cycle in the list using the Floyd's cycle-finding algorithm (also known as the tortoise and hare algorithm). It uses two pointers, slow and fast, initially set to the head. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle in the list, eventually the fast pointer will catch up to the slow pointer, indicating the presence of a cycle. If the fast pointer reaches the end of the list (fast or fast.next becomes None), it means there is no cycle in the list.

#In the test section, we create a cyclic linked list by linking the nodes together. The last node's next points back to the second node, creating a cycle. We then call the has_cycle function with the head of the linked list and print the result.