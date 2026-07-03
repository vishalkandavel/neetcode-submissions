class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = 0

        freq = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in freq:
                ans += freq[prefix - k]

            freq[prefix] = freq.get(prefix, 0) + 1

        return ans
        return count