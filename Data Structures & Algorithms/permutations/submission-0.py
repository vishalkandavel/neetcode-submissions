class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(start):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for i in range(len(nums)):

                if nums[i] in curr:
                    continue
                    
                curr.append(nums[i])
                dfs(0)
                curr.pop()

        dfs(0)
        return res
