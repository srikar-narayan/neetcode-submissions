class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target < matrix[mid][-1]:
                ml, mr = 0, len(matrix[mid]) - 1
                while ml <= mr:
                    mmid = (ml + mr) // 2
                    if matrix[mid][mmid] == target:
                        return True
                    elif matrix[mid][mmid] < target:
                        ml = mmid + 1
                    elif matrix[mid][mmid] > target:
                        mr = mmid - 1
                return False
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
        return False 
        
        