import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        ans = []
        if a > 0:
            heapq.heappush(heap,(-a,"a"))
        if b > 0:
            heapq.heappush(heap,(-b,"b"))
        if c > 0:
            heapq.heappush(heap,(-c,"c"))
        
        
        while heap:

            freq1, ch1 = heapq.heappop(heap)
        
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch1:

                if not heap:
                    break

                freq2, ch2 = heapq.heappop(heap)
                ans.append(ch2)
                freq2 = freq2 + 1

                if freq2 < 0:
                    heapq.heappush(heap,(freq2, ch2))
                
                heapq.heappush(heap,(freq1, ch1))
            
            else:
            
                ans.append(ch1) 
                freq1 = freq1 + 1

                if freq1 < 0:
                    heapq.heappush(heap,(freq1,ch1))

        return "".join(ans)



            


            
