import multiprocessing

class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        
        self.grid = grid
        
        result_matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        result = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result *= grid[i][j]
    
    
        self.result = result
        
        elements = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        
        with multiprocessing.Pool() as pool:
            result_elements = pool.starmap(self.calculate_element, [(i, j) for i, j in elements])
        
        for element in result_elements:
            i, j, element_result = element
            result_matrix[i][j] = element_result
        
        return result_matrix
    
    def calculate_element(self, i, j):
        element_result = self.result // self.grid[i][j]
        element_result = element_result % 12345
        return (i, j, element_result)
        
if __name__ == '__main__':
    
    grid = [[1,2],[3,4]]
    s = Solution()
    
    print(s.constructProductMatrix(grid))