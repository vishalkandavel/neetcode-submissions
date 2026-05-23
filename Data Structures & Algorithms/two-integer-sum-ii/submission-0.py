class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            left = 0
            ans =[]
            right = len(numbers) - 1
            while left < right:
                k = numbers[right] + numbers[left]
                if  k == target:
                    ans.extend([left + 1,right + 1 ])
                    return ans
                elif k < target :
                    left = left + 1
                else:
                    right = right - 1