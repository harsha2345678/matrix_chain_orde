import heapq


# ----------------------------------------
# Dijkstra's Algorithm
# ----------------------------------------
def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap

    Time Complexity : O((V + E) log V)
    Space Complexity: O(V)

    graph  : Dictionary representing adjacency list
    source : Starting vertex
    """

    n = len(graph)

    # Initialize distances and previous nodes
    distance = [float('inf')] * n
    previous = [None] * n

    distance[source] = 0

    # Priority Queue (distance, vertex)
    priority_queue = [(0, source)]

    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Explore all neighboring vertices
        for neighbor, weight in graph[current_vertex]:
            new_distance = distance[current_vertex] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distance, previous


# ----------------------------------------
# Reconstruct Shortest Path
# ----------------------------------------
def reconstruct_path(previous, source, destination):
    path = []

    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ----------------------------------------
# Main Program
# ----------------------------------------
def main():

    # Graph represented as an adjacency list
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }

    source = 0

    # Run Dijkstra's Algorithm
    distance, previous = dijkstra(graph, source)

    # Display Results
    print(f"\nShortest Paths from Vertex {source}\n")
    print("-" * 65)
    print(f"{'Vertex':<10}{'Distance':<15}{'Path'}")
    print("-" * 65)

    for vertex in range(len(graph)):
        path = reconstruct_path(previous, source, vertex)

        if path:
            path_string = " -> ".join(map(str, path))
        else:
            path_string = "No Path"

        if distance[vertex] == float('inf'):
            dist = "INF"
        else:
            dist = distance[vertex]

        print(f"{vertex:<10}{str(dist):<15}{path_string}")

    print("-" * 65)


# ----------------------------------------
# Driver Code
# ----------------------------------------
if __name__ == "__main__":
    main()