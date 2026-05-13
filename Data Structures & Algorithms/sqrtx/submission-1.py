class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Goal: return the integer part of the square root of x (i.e., floor(sqrt(x))).
        We must NOT use built-in sqrt or exponent functions.

        Idea: use binary search to find the largest number 'mid' such that mid*mid <= x.
        """

        # Left and right ends of our search range.
        # The square root of x is always between 0 and x (inclusive).
        l = 0
        r = x

        # 'ans' will store the best answer we have seen so far.
        # It will always be a number whose square is <= x.
        ans = 0

        # Keep searching while our range is valid.
        while l <= r:
            # Pick the middle number to check.
            # Using l + (r - l) // 2 avoids overflow in other languages (safe habit).
            mid = l + (r - l) // 2

            # Compute mid * mid once and reuse it.
            sq = mid * mid

            if sq == x:
                # Perfect square: we found an exact square root.
                return mid
            elif sq < x:
                # mid^2 is too small, so the real sqrt is bigger.
                # mid is a valid "floor" candidate, so remember it.
                ans = mid
                # Move search to the right half to try larger numbers.
                l = mid + 1
            else:
                # mid^2 is too big, so the real sqrt is smaller.
                # Move search to the left half to try smaller numbers.
                r = mid - 1

        # If we exit the loop, there is no exact square root.
        # 'ans' holds the largest mid we saw with mid^2 <= x,
        # which is exactly floor(sqrt(x)).
        return ans  
        
        