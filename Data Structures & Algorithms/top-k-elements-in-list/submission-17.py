class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = []
        for _ in range(len(nums) + 1):
            freq.append([])
            
        res = []
        
        for n, f in count.items():
            freq[f].append(n)
        for ind in range(len(nums), -1, -1):
            if freq[ind]:
                for i in freq[ind]:
                    res.append(i)
                if len(res) == k:
                    return res