class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count ={}
        max_len = 0
        maxf = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            maxf = max(maxf, count[s[right]])
            while ((right - left + 1 ) - maxf) > k:
                count[s[left]] -= 1
                left += 1
            max_len = max (max_len, right - left + 1 )   
        return max_len

        
    