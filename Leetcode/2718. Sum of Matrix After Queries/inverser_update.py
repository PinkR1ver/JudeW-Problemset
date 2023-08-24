import numpy as np

class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        
        row = np.full(n, -1)
        col = np.full(n, -1)
        row_count = 0
        col_count = 0
        ans = 0
        
        for i in range(len(queries) - 1, -1, -1):
            if row_count == n and col_count == n:
                break
            
            if queries[i][0] == 0:
                if row[queries[i][1]] == -1:
                    row[queries[i][1]] = queries[i][2]
                    ans += queries[i][2] * (n - row_count)
                    col_count += 1
            
            if queries[i][0] == 1:
                if col[queries[i][1]] == -1:
                    col[queries[i][1]] = queries[i][2]
                    ans += queries[i][2] * (n - col_count)
                    row_count += 1
        
        return ans
            
    
if __name__ == '__main__':
    n = 2
    queries = [[1,1,1],[1,0,7],[0,0,0]]
    print(Solution().matrixSumQueries(n, queries))