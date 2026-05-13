class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # We want to check if there exists an integer 'k'
        # such that k * k == num.
        # Use binary search on the possible values of k.

        l = 1              # smallest possible candidate (1^2 = 1)
        r = num            # largest possible candidate (num^2 = num*num would exceed, 
                           # so the max square root is at most 'num')

        while l <= r:
            # Pick the middle candidate
            mid = l + (r - l) // 2
            res = mid * mid  # square of candidate

            # If square is smaller, move right (we need a larger number)
            if res < num:
                l = mid + 1

            # If square is larger, move left (we need a smaller number)
            elif res > num:
                r = mid - 1

            # If exact match, num is a perfect square
            else:
                return True

        # If loop ends, no integer square root was found
        return False              
        