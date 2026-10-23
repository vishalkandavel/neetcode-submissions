class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
            result = []
            curr = []
            def dfs(start, rem):
                if rem == 0:
                    result.append(curr.copy())
                    return 
                
                if rem < 0:
                    return

                for i in range (start, len(nums)):
                    curr.append(nums[i])
                    dfs(i, rem - nums[i])
                    curr.pop()
            
            dfs(0, target)
            return result

                    