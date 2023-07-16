
#Problem:
#Implement a queue using two stacks. The queue should support the following operations:

#enqueue(value): Add an element to the end of the queue.
#dequeue(): Remove and return the element at the front of the queue.
#is_empty(): Check if the queue is empty.

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, value):
        self.stack1.append(value)
    def dequeue(self):
        if self.is_empty():
            return None
#Move elements from stack1 to stak2 in reverse order
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        # Retrieve the front elements from stack1 
        front = self.stack1.pop()
        #Move elements back form stak2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return front
    def is_empty(self):
        return len(self.stack1) == 0
    
# Test the queue Implementation
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  #Returns 1
    print(queue.is_empty())  # Return false
    
#Explanation:

#Queue class: This class represents the queue implemented using two stacks. It has two attributes, stack1 and stack2, which are used as the main stacks to store the elements of the queue.

#enqueue method: This method takes a value and adds it to the end of the queue. It simply appends the value to stack1, as it represents the rear end of the queue.

#dequeue method: This method removes and returns the element at the front of the queue. It checks if the queue is empty using the is_empty method. If the queue is not empty, it transfers the elements from stack1 to stack2 in reverse order, with the front element of the queue ending up at the top of stack2. Then, it removes and returns the front element from stack1. Finally, it transfers the remaining elements from stack2 back to stack1.

#is_empty method: This method checks if the queue is empty by examining the size of stack1.

#In the test section, we create an instance of the Queue class called queue. We then enqueue three elements (1, 2, and 3) and demonstrate dequeuing the front element using dequeue. Finally, we check if the queue is empty using the is_empty method.