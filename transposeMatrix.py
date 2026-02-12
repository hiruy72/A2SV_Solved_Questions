class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row  = len(matrix)
        colmn= len(matrix[0])

        c= [[0] *row for _ in range(colmn)]

        for i in range(colmn):
            for j in range(row):
                c[i][j] = matrix[j][i]
        return c
