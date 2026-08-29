class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for p in (2, 3, 5):
            while n % p == 0:
                n //= p

        return n == 1


# Time Complexity = O(log n)
# Space complexity = O(1)

# You can test it by creating an instance of the Solution class:
# sol = Solution()
# print(f"Is 6 an ugly number? {sol.isUgly(6)}")
# print(f"Is 1 an ugly number? {sol.isUgly(1)}")