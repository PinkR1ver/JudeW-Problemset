class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        
        result = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result *= grid[i][j]
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = result // grid[i][j]
                grid[i][j] = grid[i][j] % 12345
                
        return grid
    
if __name__ == '__main__':
    
    grid = [[1,2],[3,4]]
    s = Solution()
    
    print(s.constructProductMatrix(grid))