class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        letters = []
        for _ in range(len(nums) + 1):
            letters.append([])
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for l, f in freq.items():
            letters[f].append(l)
        for ind in range(len(nums), -1, -1):
            if letters[ind]:
                res += letters[ind]
                if len(res) == k:
                    return res