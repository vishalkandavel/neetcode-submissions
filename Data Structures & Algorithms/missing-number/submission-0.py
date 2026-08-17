class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)
        result = total

        for index in range(total):
            result ^= index
            result ^= nums[index]

        return result