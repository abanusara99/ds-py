class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def delete_node(self, key):
        """Delete the first occurrence of a node with the given key."""
        current = self.head
        
        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next  # Change head
            current = None  # Free memory
            return
        
        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # If key was not present in linked list
        if not current:
            return
        
        # Unlink the node from linked list
        prev.next = current.next
        current = None  # Free memory

    def size(self):
        """Return the size of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        """Prints the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_beginning(0)
llist.print_list() 

llist.delete_node(1)
llist.print_list() 

print(f"Size of linked list after deletion: {llist.size()}")  