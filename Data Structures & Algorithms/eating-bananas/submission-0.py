class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        left = 1
        right = max(piles)
        answer = right 
        while left <= right:
            k = ( left + right ) // 2
            ht = 0
            for pile in piles:
                ht += (pile + k - 1) // k
            if ht <= h:
                answer = k
                right = k - 1
            else:
                left = k + 1
        return answer 



            