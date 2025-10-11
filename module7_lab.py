### LAB 7 Group 1
## module7_lab.py
# Jenny Morris             [Student ID 10677217]
# Chih-Hsiang Chang        [Student ID 10669872]
# Nathaniel John Hernandez [Student ID 10731765]

# ★　todo list: queue implementation, demo queue


# NOTE: Our structures for queue and stack go directly in this file.
# Rather than submitting a zip, we only submit one py file with everything
# in it this week.

    
# PART A: STACK IMPLEMENTATION (Ticket Cancellation Management)

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

class CancellationDetails(Node):
    """
    Cancellation details to be passed to the data parameter of the node class.
    In an real-world application using this project, users could enter values.
    """

    def __init__(self, number=0000, name="NO NAME", location="NO LOCATION", m=1, d=1, y=2025, reason="NO REASON"):
        """
        Initialize a cancellation with given data.
        """

        self.number = number
        self.name = name
        self.location = location
        self.m = m
        self.d = d
        self.y = y
        self.reason = reason

    def __str__(self):
        """
        Return cancellation details as a one-line string summary.
        """
        return f"Ticket #{self.number:04d} - {self.name} - {self.location} on {self.m:02d}/{self.d:02d}/{self.y:02d} - Reason:{self.reason}"
    
class Stack:
    """
    Stack implementation using linked list for managing ticket cancellations.
    Follows LIFO (Last-In-First-Out) principle where most recent cancellations 
    are processed first.
    """
    
    def __init__(self, capacity = -1): # Negative values for capacity allow for unbounded stacks.
        """
        Initialize an empty stack with given capacity.
        """
        self.top = None # Most recent (prioritized) cancellation
        self.size = 0 # Number of cancellations to handle
        self.capacity = capacity # Capacity, or Maximum number of cancellations to allow
    
    def push(self, cancellation_details):
        """
        Add a new cancellation to the top of the stack, if there is room.
        
        Args:
            cancellation_details: Details of the ticket cancellation

        Raises:
            Exception: If the stack is is full
        """
        if self.is_full():
            raise Exception("Cannot push to full stack")
        
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
            bool: True if the stack is empty (top element is none), False otherwise
        """
        return self.top is None
    
    def is_full(self):
        """
        Check if the stack is full.
        
        Returns:
            bool: True if the stack is full (size = capacity), False otherwise
        """
        return self.size == self.capacity
    
    def get_size(self):
        """
        Get the number of cancellations in the stack.
        
        Returns:
            int: The number of elements in the stack
        """
        return self.size
    
    def get_capacity(self):
        """
        Get the capacity (max size) of the stack. Negative values = unbounded.
        
        Returns:
            int: The capacity of the stack
        """
        return self.capacity


# PART B: QUEUE IMPLEMENTATION (Customer Service Call Handling)

class CallerDetails(Node):
    """
    Caller details to be passed to value of a call in the calls array.
    In an real-world application using this project, users could enter values.
    """

    def __init__(self, id=0000, name="NO NAME",  area=555, number=5555555, issue="NO ISSUE"):
        """
        Initialize a caller with given data.
        """

        self.id = id
        self.name = name
        self.area = area
        self.number = number
        self.issue = issue

    def __str__(self):
        """
        Return caller details as a one-line string summary.
        """
        return f"Caller - ID: {self.id:04d} - Name: {self.name} - Number: ({self.area}) {self.number//10000}-{self.number%10000} - Issue: {self.issue}"

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
            initial_capacity (int): Initial capacity of the internal array
        """

        self.size = 0
        self.capacity = initial_capacity
        self.data = [0]*initial_capacity
        self.front_index = 0
    
    def enqueue(self, call_details):
        """
        Add a new customer call to the back of the queue.
        
        Args:
            call_details: Details of the customer service call
        """
        if self.get_size() == self.capacity:
            self._resize()

        self.data[(self.front_index+self.size)%self.capacity] = call_details
        self.size +=1
    
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

            self.front_index = (self.front_index + 1) % len(self.data)
            self.size -= 1

        else:
            raise Exception("Cannot remove element from an empty queue")
    
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
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise
        """

        return self.size == 0

    
    def get_size(self):
        """
        Get the number of calls in the queue.
        
        Returns:
            int: The number of elements in the queue
        """
        return self.size
    
    def get_capacity(self):
        """
        Get the current maximum capacity of the queue.
        
        Returns:
            int: The capacity of the queue
        """
        return self.capacity
    
    def _resize(self):
        """
        Private method to increase the capacity of the internal array when capacity is exceeded.
        Doubles the current capacity and copies existing elements.
        """
        new_capacity = self.capacity * 2
        new_data = [0]*new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front_index + i) % self.capacity]
        self.data = new_data
        self.front_index = 0
        self.capacity = new_capacity


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
    print(f"   Stack capacity: {cancellation_stack.get_capacity()} (negative values = unbounded)")
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

    # Sample ticket cancellations to add to stack
    cancellations = list(map(lambda x: CancellationDetails(x[0], x[1], x[2], x[3], x[4], x[5], x[6]),
                             [(1001, "John Smith", "Concert", 10, 15, 2025, "Personal emergency"),
                              (1002, "Sarah Johnson", "Theater", 10, 16, 2025, "Flight cancelled"),
                              (1003, "Mike Daves", "Sports game", 10, 17, 2025, "Work conflict"),
                              (1004, "Lisa Wilson", "Musical", 10, 18, 2025, "Illness"),
                              (1005, "Tom Brown", "Comedy Show", 10, 19, 2025, "Double booking")]))
    
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

    # Test 1: Check empty queue
    print("1. Testing empty Queue:")
    print(f"   Queue is empty: {call_queue.is_empty()}")
    print(f"   Queue size: {call_queue.get_size()}")
    print(f"   Queue capacity: {call_queue.get_capacity()}")

    #testing edge cases
    try:
        call_queue.front()
    except Exception as e:
        print(f"   Front empty queue error: {e}")
    try:
        call_queue.dequeue()
    except Exception as e:
        print(f"   Dequeue empty queue error: {e}")



    print("\n2. Enqueue call details:")
    
    # Sample incoming calls to add to stack
    calls = list(map(lambda x: CallerDetails(x[0], x[1], x[2], x[3], x[4]),
                             [(1001, "John Smith", 555, 1234567, "Billing issue"),
                              (1002, "Jane Doe", 555, 1751337, "Technical support"),
                              (3304, "Angel Gonzalez", 555, 9871234, "Internet plan")]))
    
    # Enqueue calls onto the stack
    for i, call in enumerate(calls, 1):
        call_queue.enqueue(call)
        print(f"   {i}. Queued: {call}")
        print(f"      Queue size: {call_queue.get_size()}")
        

    print(f"   Priority call: {call_queue.front()}")
    print(f"   Queue size: {call_queue.get_size()}")
    print(f"   Queue is empty: {call_queue.is_empty()}")

    print("\n3. Resizing the Queue when exceeding capacity:")
    call_queue.enqueue(CallerDetails(1003, "Mike Davis", 555, 8765309, "Account update"))
    print(f"   Add another call to exceed capacity.:  {CallerDetails(1003, "Mike Davis", 555, 8765309, "Account update")}")
    print(f"   Queue size: {call_queue.get_size()}")
    print(f"   Queue capacity: {call_queue.get_capacity()}")

    
    print("\n4. Deque call details:")
    call_queue.dequeue()
    print(f"   Priority call: {call_queue.front()}")
    print(f"   Queue size: {call_queue.get_size()}")

    print("\nStack demonstration complete.")


def main():
    """
    Main function to run demonstrations of both data structures.
    """
    print("LAB 7 - Data Structures Implementation")
    print()
    
    demonstrate_stack()
    
    print("=" * 60)
    print()
    
    demonstrate_queue()


if __name__ == "__main__":
    main()

