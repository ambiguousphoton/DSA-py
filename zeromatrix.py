class Solution:
    def zero_matrix(matrix:list[list[int]]) -> list[list[int]]:
        zeros = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j, col_block in enumerate(matrix[i]):
                if col_block == 0:
                    zeros.append([i,j])
        zero_rows = set() 
        zero_cols = set()
        for zero in zeros: 
            zero_rows.add(zero[0])
            zero_cols.add(zero[1])

        for i in range(n):
            if i in zero_rows:
                for j in range(m): matrix[i][j] = 0
            else:
                for j in range(m):
                    if j in zero_cols: matrix[i][j] = 0
        return matrix 


matrix = [[1,1,1,0,1,1,1],
          [0,1,1,1,1,0,1],
          [1,1,1,1,1,1,1],
          [1,0,1,1,1,1,1],
          [1,1,1,1,1,1,1]]
for i in matrix:
    print(i)
print("========================================")
a = Solution.zero_matrix(matrix)
for i in a:
    print(i)