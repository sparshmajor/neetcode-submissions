class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0              
        r = x
        ans = 0

        while l <= r:
            print(l,r)
            # Pick the middle candidate
            mid = l + (r - l) // 2
            print("mid",mid)
            res = mid * mid  # square of candidate

            # If square is smaller, move right (we need a larger number)
            if res < x:
                ans = mid
                l = mid + 1

            # If square is larger, move left (we need a smaller number)
            elif res > x:
                r = mid - 1

            elif res == x:
                return mid
        return ans        
        
        