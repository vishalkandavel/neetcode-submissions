class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        candidates.sort()
        def dfs(start, rem):

            if rem == 0:
                result.append(curr.copy())
                return
            
            if rem < 0:
                return 

            for i in range(start, len(candidates)):

                if i>start and candidates[i] == candidates[i-1]:
                    continue

                curr.append(candidates[i])
                dfs(i+1, rem - candidates[i])
                curr.pop()

        dfs(0, target)
        return result
