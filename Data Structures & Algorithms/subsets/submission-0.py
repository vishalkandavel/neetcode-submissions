class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_subs = []
            for sub in res:
                new_sub = sub + [num]
                new_subs.append(new_sub)
            
            res.extend(new_subs)
        return res