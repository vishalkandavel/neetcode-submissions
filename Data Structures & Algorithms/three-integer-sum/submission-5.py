class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            result = []
            seen = set()
            for i in range(len(nums)):
                left = i+1
                right = len(nums) - 1
                nums.sort()
                while left < right:
                    sum = nums[left] + nums[right] + nums[i]
                    if sum == 0:
                        triplet = tuple([nums[i], nums[left], nums[right]])
                        left = left + 1
                        right = right - 1
                        if triplet not in seen:
                            seen.add(triplet)
                            result.append(list(triplet))
                    elif sum < 0:
                        left = left + 1
                    else:
                        right = right - 1
                    
            return result