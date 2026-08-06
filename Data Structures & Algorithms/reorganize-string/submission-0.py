from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        heap = []
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))

        prev_freq, prev_char = 0, ""
        ans = []

        while heap:
            freq, ch = heapq.heappop(heap)

            ans.append(ch)
            freq += 1

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_freq, prev_char = freq, ch

        if len(ans) != len(s):
            return ""

        return "".join(ans)