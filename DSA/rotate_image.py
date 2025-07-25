
    def rotate(self, matrix: List[List[int]]) -> None:
    
        n = len(matrix)

        # Step 1: Transpose the matrix (swap rows with columns)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
