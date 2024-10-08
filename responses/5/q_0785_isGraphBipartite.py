class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # Dictionary to assign colors to nodes
        queue = collections.deque()  # Queue for BFS

        for node in range(len(graph)):
            if node in color:  # If node already colored, continue
                continue

            color[node] = 0  # Color node with 0
            queue.append(node)  # Add node to queue

            while queue:
                current = queue.popleft()  # Get node from queue

                for neighbor in graph[current]:  # Explore neighbors
                    if neighbor not in color:  # If neighbor not colored
                        color[neighbor] = 1 - color[current]  # Color neighbor with opposite color
                        queue.append(neighbor)  # Add neighbor to queue
                    elif color[neighbor] == color[current]:  # If neighbor has same color as current node
                        return False

        return True   