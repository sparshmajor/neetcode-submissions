class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the search boundaries (left = 0, right = last index)
        l = 0
        r = len(nums) - 1

        # Continue searching while the range is valid
        while l <= r:
            # Find the middle index (avoid overflow in other languages with l+(r-l)//2)
            mid = l + (r - l) // 2

            # If target is greater, discard left half (including mid)
            if nums[mid] < target:
                l = mid + 1

            # If target is smaller, discard right half (including mid)
            elif nums[mid] > target:
                r = mid - 1

            # If target is exactly found, return its index
            else:
                return mid

        # If not found, l will be pointing to the "insertion position".
        # Another way: return l directly.
        # Here r+1 == l at this point, so both are correct.
        return r + 1              

        