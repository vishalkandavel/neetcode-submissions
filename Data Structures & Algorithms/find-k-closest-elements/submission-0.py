class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for i in range(len(arr)):
            arr.sort(key=lambda n: (abs(n - x), n))
            ans = arr[:k]
            ans.sort()            
            return ans