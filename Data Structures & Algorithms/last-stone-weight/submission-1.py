import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i,stone in enumerate(stones):
            heapq.heappush(heap,-stone)

        while len(heap) > 1:

            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            diff = y - x

            if (diff == 0):
                continue
            heapq.heappush(heap,diff)   

        return -heap[0] if heap else 0

        
        

        

        