# Given an integer target, return true if target is in matrix or false otherwise.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1 # len of all the numbers in the matrix
        if rows == 0 or target is None:
            return False

        while l <= r:
            mid = (l+r) // 2
            num = matrix[mid // cols][mid % cols] # matrix way of finding rows and cols indices
            if  num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
