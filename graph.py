# Create a graph
graph = {}
print("Initial graph:", graph)

# Add vertices
graph['A'] = []
graph['B'] = []
print("Graph after adding vertices A and B:", graph)

# Add edges
graph['A'].append('B')
graph['B'].append('A')
print("Graph after adding edge between A and B:", graph)

# Remove vertex 'B'
del graph['B']
print("Graph after removing vertex B:", graph)

# Attempt to remove edge between 'A' and 'B'
# This will fail since B has already been removed
try:
    graph['A'].remove('B')  # Note: This will fail if B is already removed
except KeyError:
    print("Attempted to remove edge between A and B, but B is already removed.")

# Get all vertices
vertices = list(graph.keys())
print("Vertices in the graph:", vertices)

# Get all edges
edges = [(u, v) for u in graph for v in graph[u] if (v, u) not in edges]
print("Edges in the graph:", edges)

# Check if vertex exists
exists_vertex = 'A' in graph
print("Does vertex A exist?", exists_vertex)

# Check if edge exists
exists_edge = 'A' in graph and 'B' in graph['A']
print("Does edge A-B exist?", exists_edge)