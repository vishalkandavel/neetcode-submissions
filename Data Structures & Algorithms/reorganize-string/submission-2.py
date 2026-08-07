from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        ans = []
        prev_freq = 0
        prev_ch = ""


        for ch,freq in count.items():
            heapq.heappush(heap, (-freq,ch))
        
        while heap:

            freq, ch = heapq.heappop(heap)
            ans.append(ch)
            freq = freq + 1 

            if prev_freq < 0:
                heapq.heappush(heap,(prev_freq, prev_ch))
            
            prev_freq, prev_ch = freq,ch

        if len(ans) != len(s):
            return ""

        return "".join(ans)