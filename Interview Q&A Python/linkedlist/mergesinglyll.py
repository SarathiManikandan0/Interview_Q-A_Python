#Problem:
#Given two sorted linked lists, write a function to merge them into a single sorted linked list. Return the head of the merged list.

#Example:
#Input:
#List 1: 1 -> 3 -> 5
#List 2: 2 -> 4 -> 6
#Output:
#Merged List: 1 -> 2 -> 3 -> 4 -> 5 -> 6

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def merge_lists(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    if head1.data <= head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next
        
    current = merged_head
    
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        
        current = current.next
    if head1:
        current.next = head1
    if head2:
        current.next = head2
    
    return merged_head
if __name__ == "__main__":
    list1_head = Node(1)
    list1_head.next = Node(2)
    list1_head.next.next = Node(5)
    
    list2_head = Node(2)
    list2_head.next = Node(4)
    list2_head.next.next = Node(6)
    
    merged_head = merge_lists(list1_head, list2_head)
    
    #Display the merged list
    
    current = merged_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
            
#Node class: Same as before, this class represents a node in the linked list.

#merge_lists function: This function takes the heads of two sorted linked lists as input and merges them into a single sorted linked list. It uses a merging technique similar to the merge step in merge sort. The function starts by comparing the data values of the first nodes in both lists. It selects the smaller value as the head of the merged list and advances the corresponding pointer (head1 or head2). Then, it iteratively compares the data values of the next nodes in both lists and appends the smaller value to the merged list. Finally, it appends the remaining nodes of the list that still has elements left.

#In the test section, we create two sorted linked lists (list1_head and list2_head). We then call the merge_lists function with the heads of the two lists and assign the merged head to merged_head. We display the merged list by iterating through the nodes starting from the merged head.
            
        