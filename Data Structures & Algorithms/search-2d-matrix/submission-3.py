class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = {}
        for index, element in enumerate(matrix):
            mat[index] = max(element)
        
        l, r = 0, len(matrix) - 1
        while l <= r:
            if target > mat[l]:
                l += 1
            elif target <= mat[l]:
                ll, rr = 0, len(matrix[l]) -1
                while ll <= rr:
                    mid = (ll + rr) // 2
                    if target > matrix[l][mid]:
                        ll = mid + 1
                    elif target < matrix[l][mid]:
                        rr = mid -1
                    else:
                        return True
                return False
        return False