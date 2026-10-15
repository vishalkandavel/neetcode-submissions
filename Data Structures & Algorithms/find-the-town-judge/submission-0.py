class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d_out = {}
        d_in = {}
        for i in range(1,n+1):
            d_in[i] = 0
            d_out[i] = 0
        for pair in trust:
            a,b = pair
            d_out[a] += 1
            d_in [b] += 1

        for k in range(1,n+1):
            if d_in[k] == n-1 and d_out[k] ==0:
                return k 
        
        return -1
