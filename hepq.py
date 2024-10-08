import heapq

# Create an empty list to represent the heap
min_heap = []

# heap min- the parent node is always less than or equal to its child nodes. 
#This means that the smallest element is always at the root of the tree.
# Adding elements to the heap
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

# Displaying the heap
print("Heap after adding elements:", min_heap)

# Removing and returning the smallest element
smallest = heapq.heappop(min_heap)
print("Removed smallest element:", smallest)

# Displaying the heap after removal
print("Heap after removing smallest element:", min_heap)

# Converting a list into a heap
numbers = [21, 1, 45, 78, 3, 5]
heapq.heapify(numbers)
print("Heap created from list:", numbers)