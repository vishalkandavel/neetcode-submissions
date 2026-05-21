class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        lp = 1
        for i in range(len(nums)):
            left.append(lp)
            lp = lp * nums[i]
        rp = 1
        for i in range(len(nums)-1,-1,-1):
            right.append(rp)
            rp = rp * nums [i]
        result = []
        right.reverse()
        for i in range(len(nums)):
            result.append(left[i]*right[i])
        return result
