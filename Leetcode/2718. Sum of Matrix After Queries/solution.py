import numpy as np

class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        
        matrix = np.zeros((n,n))
        for query in queries:
            if query[0] == 0:
                matrix[query[1]] = query[2]
            if query[0] == 1:
                matrix[:,query[1]] = query[2]
                
        return int(np.sum(matrix))
    
if __name__ == '__main__':
    n = 8
    queries = [[0,6,30094],[0,7,99382],[1,2,18599],[1,3,49292],[1,0,81549],[1,1,38280],[0,0,19405],[0,4,30065],[1,4,60826],[1,5,9241],[0,5,33729],[0,1,41456],[0,2,62692],[0,3,30807],[1,7,70613],[1,6,9506],[0,5,39344],[1,0,44658],[1,1,56485],[1,2,48112],[0,6,43384]]
    print(Solution().matrixSumQueries(n, queries))