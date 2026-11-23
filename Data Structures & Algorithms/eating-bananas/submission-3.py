class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                res = mid
                r = mid - 1
        return res