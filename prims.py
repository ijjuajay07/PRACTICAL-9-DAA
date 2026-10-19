import heapq

def primMST(V, adj):
    # Min-heap to store (weight, node)
    pq = []

    # Initialize arrays
    key = [float('inf')] * V
    parent = [-1] * V
    inMST = [False] * V

    # Start with vertex 0
    src = 0
    heapq.heappush(pq, (0, src))
    key[src] = 0

    mst_weight = 0

    while pq:
        weight, u = heapq.heappop(pq)

        # Skip if vertex is already included
        if inMST[u]:
            continue

        # Include vertex in MST
        inMST[u] = True
        mst_weight += weight

        # Traverse adjacent vertices
        for weight_uv, v in adj[u]:
            if not inMST[v] and weight_uv < key[v]:
                key[v] = weight_uv
                heapq.heappush(pq, (key[v], v))
                parent[v] = u

    # Print MST edges
    print("Edges in the Minimum Spanning Tree:")

    for i in range(1, V):
        if parent[i] != -1:
            print(parent[i], "-", i)

    print("Total Weight of MST:", mst_weight)
     


def main():
    V = 5
    adj = [[] for _ in range(V)]

    # Add edges: (weight, neighbor)

    adj[0].append((2, 1))
    adj[1].append((2, 0))

    adj[0].append((3, 3))
    adj[3].append((3, 0))

    adj[1].append((3, 2))
    adj[2].append((3, 1))

    adj[1].append((5, 4))
    adj[4].append((5, 1))

    adj[2].append((7, 4))
    adj[4].append((7, 2))

    adj[3].append((6, 4))
    adj[4].append((6, 3))

    primMST(V, adj)


if __name__ == "__main__":
    main()
