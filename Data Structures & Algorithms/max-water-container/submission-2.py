class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curr_vol = (r - l) * min(heights[r], heights[l])
            max_vol = max(max_vol, curr_vol)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_vol

        