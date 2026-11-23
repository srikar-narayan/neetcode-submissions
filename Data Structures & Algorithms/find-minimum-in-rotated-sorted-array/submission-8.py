class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find mid
        #if mid > right -> go right
        #if mid < right -> go left

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

        