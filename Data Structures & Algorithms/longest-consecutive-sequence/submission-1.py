class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        numset = set(nums)
        for num in numset:
            if (num - 1) in numset:
                continue
            else:
                current_length = 1
                while num + current_length in numset:
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length
