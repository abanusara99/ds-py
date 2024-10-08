class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def insert_child(parent_node, child_data):
    child_node = Node(child_data)
    parent_node.children.append(child_node)

def traverse(node):
    print(node.data)
    for child in node.children:
        traverse(child)

def find_node(node, target):
    if node.data == target:
        return node
    for child in node.children:
        result = find_node(child, target)
        if result:
            return result
    return None

def delete_child(parent_node, child_data):
    parent_node.children = [child for child in parent_node.children if child.data != child_data]

def get_height(node):
    if not node.children:
        return 1
    return 1 + max(get_height(child) for child in node.children)

def get_size(node):
    size = 1  # Count the current node
    for child in node.children:
        size += get_size(child)
    return size

# Example usage:
root = Node("Root")
insert_child(root, "Child 1")
insert_child(root, "Child 2")
insert_child(root.children[0], "Child 1.1")
insert_child(root.children[0], "Child 1.2")

print("Tree Traversal:")
traverse(root)  # Output: Root -> Child 1 -> Child 1.1 -> Child 1.2 -> Child 2

print(f"Size of tree: {get_size(root)}")  # Output: Size of tree: 5

print(f"Height of tree: {get_height(root)}")  # Output: Height of tree: 3

delete_child(root, "Child 2")
print("Tree after deletion:")
traverse(root)  # Output will not include Child 2