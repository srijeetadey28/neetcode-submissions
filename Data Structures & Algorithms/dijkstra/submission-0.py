import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Step 1: Build the adjacency list
        adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Step 2: Initialize min-heap and distances
        # Heap stores tuples of (current_distance, node)
        min_heap = [(0, src)]
        shortest = {}
        
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            
            # If already visited with a shorter or equal distance, continue
            if n1 in shortest:
                continue
                
            shortest[n1] = w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, (w1 + w2, n2))
                    
        # Step 3: Ensure all nodes from 0 to n-1 are present, setting unreachable nodes to -1
        result = {}
        for i in range(n):
            result[i] = shortest.get(i, -1)
            
        return result