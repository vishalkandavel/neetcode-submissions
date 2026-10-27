class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        final_res =[]
        def dfs(start):

            if len(res) == k:
                final_res.append(res.copy())
                return

            for i in range(start, n+1):
                res.append(i)
                dfs(i+1)
                res.pop()
        
        dfs(1)
        return final_res

