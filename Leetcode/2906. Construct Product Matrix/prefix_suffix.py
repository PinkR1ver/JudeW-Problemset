from itertools import accumulate

class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        vals = [x for row in grid for x in row]
        mul = lambda x, y: x * y % 12345
        
        pre_accu = list(accumulate(vals, mul, initial=1))
        suf_accu = list(accumulate(reversed(vals), mul, initial=1))
        
        for i in range(row_len):
            for j in range(col_len):
                grid[i][j] = mul(pre_accu[i * col_len + j], suf_accu[row_len * col_len - 1 - (i * col_len + j)])
                
        return grid

if __name__ == '__main__':
    
    grid = [[1,2],[3,4]]
    s = Solution()
    
    print(s.constructProductMatrix(grid))               