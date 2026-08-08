import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        heap = []
        trips.sort(key=lambda x: x[1])
        current = 0
     
        for passengers, start, end in trips:

            while heap and heap[0][0] <= start:

                 drop,people = heapq.heappop(heap)
                 current = current - people
            
            current = current + passengers
            if current > capacity:
                
                return False

            heapq.heappush(heap,(end,passengers))

        return True 
