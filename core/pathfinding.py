import sys
import heapq

def dijkstra(adj, src):
    V = len(adj)
    pq = []
    dist = [sys.maxsize] * V
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
