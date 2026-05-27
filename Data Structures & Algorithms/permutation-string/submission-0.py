class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            count1 = {}
            for i in range(len(s1)):
                if s1[i] in count1:
                    count1[s1[i]] += 1
                else:
                    count1[s1[i]] = 1
            left = 0
            count2 = {}
            for right in range(len(s2)):
                if s2[right] in count2:
                    count2[s2[right]] += 1
                else:
                    count2[s2[right]] = 1
                while (right - left + 1) > len(s1):
                    count2[s2[left]] -= 1
                    if count2[s2[left]] == 0:
                        del count2[s2[left]]
                    left = left + 1
                if count1 == count2:
                    return True
            return False