class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        bit = 0
        n -= 1

        while n:
            if (x & (1 << bit)) == 0:
                if n & 1:
                    ans |= (1 << bit)
                n >>= 1

            bit += 1
        return ans