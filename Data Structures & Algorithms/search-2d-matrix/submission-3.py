class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        column = len(matrix[0])
        left = 0 
        right = ( rows * column ) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // column
            col = mid % column
            value = matrix[row][col]
            if target == value:
                return True
            elif value < target :
                left = mid + 1
            else:
                right = mid - 1
        return False