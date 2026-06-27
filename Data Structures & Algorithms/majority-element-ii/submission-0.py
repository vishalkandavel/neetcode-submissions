class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        ans =[]
        for num in count:
            if count[num] > len(nums) // 3:
                ans.append(num)
        return ans

