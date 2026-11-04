class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            return total

        slow = n
        fast = n

        while fast != 1 and get_next(fast) != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if slow == fast:
                return False

        return True
