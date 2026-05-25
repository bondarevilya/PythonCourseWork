import sys
import heapq

class Pathfinder:
    @staticmethod
    def dijkstra(adj, src: int):
        V = len(adj)

        pq = []
        dist = [sys.maxsize] * V
        prev = [-1] * V

        dist[src] = 0
        heapq.heappush(pq, (0, src))

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                new_distace = dist[u] + w
                if dist[u] + w < dist[v]:
                    dist[v] = new_distace
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))

        return dist, prev

    @ staticmethod
    def reconstruct_path(prev, target):
        path = []
        current = target

        while current != -1:
            path.append(current)
            current = prev[current]

        path.reverse()
        return path