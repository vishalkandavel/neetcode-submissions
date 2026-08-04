import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = Counter(tasks)

        for freq in count.values():
            heap.append(-freq)
        
        heapq.heapify(heap)
        queue = deque()
        time = 0 

        while heap or queue:

            time = time + 1
            if heap:

                freq = 1 + heapq.heappop(heap)
                if freq != 0:

                    queue.append((freq,time+n))

            if queue and queue[0][1] == time:
                    
                heapq.heappush(heap,queue.popleft()[0])
            
        return time



       
        
        