
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a & (1 << 31):
            a -= 1 << 32

        return a
