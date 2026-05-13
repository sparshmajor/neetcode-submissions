class Solution:
    def arrangeCoins(self, n: int) -> int:
        # We are looking for the no. of rows
        # so the approach here is, we will try to keep guessing the answer 
        
        l = 1              # left boundary (minimum possible rows = 1)
        r = n              # right boundary (max possible rows = n, in case n=1+2+...+n)
        ans = 1            # store the result (max valid complete rows found so far)

        # Binary search between l and r
        while l <= r:
            # Pick the middle candidate number of rows
            mid = l + (r - l) // 2

            # Sum of first 'mid' rows (formula for arithmetic series)
            res = (mid * (mid + 1)) // 2

            # Case 1: If the sum exceeds n, too many coins used → shrink to left side
            if res > n:
                r = mid - 1

            # Case 2: If the sum fits, mid rows are possible → save and try for more
            else:
                ans = mid       # mid is valid, update answer
                l = mid + 1     # search in the right side for larger k

        # When loop ends, ans contains the maximum k rows we can build completely
        return ans       



        