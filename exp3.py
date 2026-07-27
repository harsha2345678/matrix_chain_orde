import heapq


# -----------------------------
# Union-Find (Disjoint Set)
# -----------------------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by Rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


# -----------------------------
# Kruskal's Algorithm
# -----------------------------
def kruskal(n, edges):
    edges.sort()  # Sort edges based on weight

    uf = UnionFind(n)
    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


# -----------------------------
# Prim's Algorithm
# -----------------------------
def prim(n, adj, start=0):
    INF = float('inf')

    key = [INF] * n
    parent = [-1] * n
    in_mst = [False] * n

    key[start] = 0
    priority_queue = [(0, start)]

    mst = []
    total_cost = 0

    while priority_queue:
        weight, u = heapq.heappop(priority_queue)

        if in_mst[u]:
            continue

        in_mst[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            total_cost += weight

        for v, wt in adj.get(u, []):
            if not in_mst[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(priority_queue, (wt, v))

    return mst, total_cost


# -----------------------------
# Main Program
# -----------------------------
def main():
    n = 7

    edges = [
        (7, 0, 1),
        (5, 0, 3),
        (8, 1, 2),
        (9, 1, 3),
        (7, 1, 4),
        (5, 2, 4),
        (15, 3, 4),
        (6, 3, 5),
        (8, 4, 5),
        (9, 4, 6),
        (11, 5, 6)
    ]

    # Create adjacency list
    adj = {}

    for weight, u, v in edges:
        adj.setdefault(u, []).append((v, weight))
        adj.setdefault(v, []).append((u, weight))

    # Kruskal's Algorithm
    kruskal_mst, kruskal_cost = kruskal(n, edges[:])

    # Prim's Algorithm
    prim_mst, prim_cost = prim(n, adj)

    # Display Kruskal's Result
    print("===== Kruskal's Minimum Spanning Tree =====")
    for u, v, w in kruskal_mst:
        print(f"Edge ({u} - {v})  Weight = {w}")

    print(f"\nTotal MST Cost = {kruskal_cost}")

    # Display Prim's Result
    print("\n===== Prim's Minimum Spanning Tree =====")
    for u, v, w in prim_mst:
        print(f"Edge ({u} - {v})  Weight = {w}")

    print(f"\nTotal MST Cost = {prim_cost}")


# -----------------------------
# Driver Code
# -----------------------------
if __name__ == "__main__":
    main()