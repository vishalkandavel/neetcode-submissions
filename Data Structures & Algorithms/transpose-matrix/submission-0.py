class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        column = len(matrix[0])
        res = []

        for i in range(column):
            new_row = []
            for j in range(rows):
                new_row.append(matrix[j][i])
            res.append(new_row)

        return res
                
