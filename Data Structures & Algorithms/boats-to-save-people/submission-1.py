class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            c = 0
            people.sort()
            left = 0 
            right = len(people) - 1
            while left < right:
                if people[left] + people[right] <= limit:
                    left = left + 1
                    right = right - 1
                else :
                    right = right - 1 
                c = c + 1
            if left == right :
                c = c + 1
            return c