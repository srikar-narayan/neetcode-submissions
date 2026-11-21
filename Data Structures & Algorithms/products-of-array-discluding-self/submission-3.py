class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        is0 = False
        for num in nums:
            if num == 0:
                if is0:
                    return [0]*len(nums)
                is0 = True
            else:
                product *= num
        res = [product] * len(nums)

        if is0:
            res = [0] * len(nums)
        for i in range(len(res)):
            if nums[i] == 0:
                res[i] = product
            else:
                res[i] = res[i] // nums[i]
        return res