### LAB 7 Group 1
## module7_lab.py
# Jenny Morris             [Student ID 10677217]
# Chih-Hsiang Chang        [Student ID 10669872]
# Nathaniel John Hernandez [Student ID 10731765]

# ★　todo list: queue implementation, demo queue


# NOTE: Our structures for queue and stack go directly in this file.
# Rather than submitting a zip, we only submit one py file with everything
# in it this week.


class Node:
    """
    Node class for the linked list implementation of the stack.
    Each node contains cancellation details and a reference to the next node.
    """
    def __init__(self, data):
        """
        Initialize a new node with cancellation details.
        
        Args:
            data: The cancellation details to store in this node
        """
        self.data = data
        self.next = None  # Reference to the next node in the stack
    
# PART A: STACK IMPLEMENTATION (Ticket Cancellation Management)

class Stack:
    """
    Stack implementation using linked list for managing ticket cancellations.
    Follows LIFO (Last-In-First-Out) principle where most recent cancellations 
    are processed first.
    """
    
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.top = None
        self.size = 0
    
    def push(self, cancellation_details):
        """
        Add a new cancellation to the top of the stack.
        
        Args:
            cancellation_details: Details of the ticket cancellation
        """
        new_node = Node(cancellation_details)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        """
        Remove and return the most recent cancellation from the stack.
        
        Returns:
            The cancellation details from the top of the stack
            
        Raises:
            Exception: If the stack is empty
        """
        if self.is_empty():
            raise Exception("Cannot pop from empty stack")
        
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def peek(self):
        """
        Return the most recent cancellation without removing it from the stack.
        
        Returns:
            The cancellation details from the top of the stack
            
        Raises:
            Exception: If the stack is empty
        """
        if self.is_empty():
            raise Exception("Cannot peek empty stack")
        
        return self.top.data
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise
        """
        return self.top is None
    
    def get_size(self):
        """
        Get the number of cancellations in the stack.
        
        Returns:
            int: The number of elements in the stack
        """
        return self.size


# PART B: QUEUE IMPLEMENTATION (Customer Service Call Handling)

class Queue:
    """
    Queue implementation using array-based approach for managing customer service calls.
    Follows FIFO (First-In-First-Out) principle where calls are handled in the order
    they are received.
    """
    
    def __init__(self, initial_capacity=10):
        """
        Initialize an empty queue with specified initial capacity.
        
        Args:
            initial_capacity (int): Initial size of the internal array
        """

        self.size = initial_capacity
        self.length = 0
        self.data = [0]*initial_capacity
        self.front_index = 0

        pass
    
    def enqueue(self, call_details):
        """
        Add a new customer call to the back of the queue.
        
        Args:
            call_details: Details of the customer service call
        """

        if self.get_size() == self.size:
            self.resize()

        self.data[(self.front_index+self.length)%self.size] = call_details
        self.length +=1

        pass
    
    def dequeue(self):
        """
        Remove and return the oldest call from the front of the queue.
        
        Returns:
            The call details from the front of the queue
            
        Raises:
            Exception: If the queue is empty
        """
        if not self.is_empty():
            item = self.data[self.front_index]
            self.front_index +=1
            self.front_index = (self.front_index + 1) % len(self.data)

        else:
            raise Exception("Cannot remove element from an empty queue")


        pass
    
    def front(self):
        """
        Return the oldest call without removing it from the queue.
        
        Returns:
            The call details from the front of the queue
            
        Raises:
            Exception: If the queue is empty
        """
        if not self.is_empty():
            return self.data[self.front_index]

        else:
            raise Exception("Cannot view and empty list")


        pass
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise
        """

        if self.length == 0:
            return True
        else:
            return False

        pass
    
    def get_size(self):
        """
        Get the number of calls in the queue.
        
        Returns:
            int: The number of elements in the queue
        """

        return self.length
        pass
    
    def resize(self):
        """
        Private method to resize the internal array when capacity is exceeded.
        Doubles the current capacity and copies existing elements.
        """

        new_size = self.size * 2
        new_data = [0]*new_size
        for i in range(self.length):
            new_data[i] = self.data[(self.front_index + i) % self.size]
        self.data = new_data
        self.front_index = 0
        self.size = new_size

    

        pass

 

# =============================================================================
# DEMONSTRATION AND EXAMPLE USAGE
# =============================================================================

def demonstrate_stack():
    """
    Demonstrate the stack functionality with ticket cancellation examples.
    Shows LIFO processing of cancellations.
    """
    print("Stack Demonstration:")
    
    # Create a new stack for managing ticket cancellations
    cancellation_stack = Stack()
    
    # Test 1: Check empty stack
    print("1. Testing empty stack:")
    print(f"   Stack is empty: {cancellation_stack.is_empty()}")
    print(f"   Stack size: {cancellation_stack.get_size()}")
    
    # Test edge case: try to peek/pop empty stack
    try:
        cancellation_stack.peek()
    except Exception as e:
        print(f"   Peek empty stack error: {e}")
    
    try:
        cancellation_stack.pop()
    except Exception as e:
        print(f"   Pop empty stack error: {e}")
    
    print("\n2. Adding cancellations to the stack (push operations):")
    
    # Sample ticket cancellations
    cancellations = [
        "Ticket #1001 - John Smith - Concert on 10/15/2025 - Reason: Personal emergency",
        "Ticket #1002 - Sarah Johnson - Theater on 10/16/2025 - Reason: Flight cancelled", 
        "Ticket #1003 - Mike Davis - Sports game on 10/17/2025 - Reason: Work conflict",
        "Ticket #1004 - Lisa Wilson - Musical on 10/18/2025 - Reason: Illness",
        "Ticket #1005 - Tom Brown - Comedy show on 10/19/2025 - Reason: Double booking"
    ]
    
    # Push cancellations onto the stack
    for i, cancellation in enumerate(cancellations, 1):
        cancellation_stack.push(cancellation)
        print(f"   {i}. Pushed: {cancellation}")
        print(f"      Stack size: {cancellation_stack.get_size()}")
    
    print(f"\n3. Current stack status:")
    print(f"   Stack is empty: {cancellation_stack.is_empty()}")
    print(f"   Stack size: {cancellation_stack.get_size()}")
    print(f"   Most recent cancellation (peek): {cancellation_stack.peek()}")
    
    print("\n4. Processing cancellations (pop operations) - LIFO order:")
    
    # Process cancellations in LIFO order
    cancellation_count = 1
    while not cancellation_stack.is_empty():
        processed_cancellation = cancellation_stack.pop()
        print(f"   {cancellation_count}. Processing: {processed_cancellation}")
        print(f"      Remaining in stack: {cancellation_stack.get_size()}")
        cancellation_count += 1
    
    print(f"\n5. Final stack status:")
    print(f"   Stack is empty: {cancellation_stack.is_empty()}")
    print(f"   Stack size: {cancellation_stack.get_size()}")
    
    print("\nStack demonstration complete.")


def demonstrate_queue() -> None:
    """
    Demonstrate the queue functionality with customer service call examples.
    Shows FIFO processing of calls.
    """

    call_queue = Queue(3)


    print("1. Testing empty Queue:")
    print(f"   Queue is empty: {call_queue.is_empty()}")
    print(f"   Queue size: {call_queue.get_size()}")

    print("2. Enque call details:")
    call_queue.enqueue("Caller: John Smith, Caller ID: 1001, Issue: Billing issue")
    call_queue.enqueue("Caller: Jane Doe, Caller ID: 1002, Issue: Technical support")
    call_queue.enqueue("Caller: Angel Gonzolez, Caller ID: 3304, Issue: Internet plan")

    print(call_queue.front())
    print(f"   Queue size: {call_queue.get_size()}")
    print(f"   Queue is empty: {call_queue.is_empty()}")

    print("3. Resizing the Queue:")
    call_queue.enqueue("Caller: Mike Davis, Caller ID: 1003, Issue: Account update")
    print(call_queue.front())
    print(f"   Queue size: {call_queue.get_size()}")
    
    print("4. Deque call details:")
    call_queue.dequeue()
    print(call_queue.front())
    print(f"   Queue size: {call_queue.get_size()}")

    #print(f"Caller: John Smith, Caller ID: 1001, Issue: Billing issue")

    pass


def main():
    """
    Main function to run demonstrations of both data structures.
    """
    print("LAB 7 - Data Structures Implementation")
    print()
    
    demonstrate_stack()
    
    print("=" * 60)
    print()
    for i in range(10):
        print()
    
    demonstrate_queue()


if __name__ == "__main__":
    main()

