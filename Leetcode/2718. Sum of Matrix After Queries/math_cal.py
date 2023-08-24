import numpy as np

class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        
        col = []
        row = []
        key_point = []
        
        ans = 0
        
        for query in queries:
            if query[0] == 0:
                row_val = [query[1], query[2]]
                if row_val not in row:
                    row.append(row_val)
                    ans += query[2] * n
                    if col != []:
                        for col_index in col:
                            point = [query[1], col_index[0], col_index[1]]
                            if point not in key_point:
                                key_point.append([query[1], col_index[0], col_index[1]])
                                ans -= col_index[1]
                            elif point in key_point:
                                ans -= key_point[key_point.index(point)][2]
                                key_point[key_point.index(point)][2] = col_index[1]
                
                elif row_val in row:
                    ans += query[2] * n
                    ans -= row[row.index(row_val)][1] * n
                    for index in range(len(key_point)):
                        if key_point[index][0] == query[1]:
                            ans += row[row.index(row_val)][1]
                            ans -= key_point[index][2]
                            key_point[index][2] = row[row.index(row_val)][1]
                        
                    
            if query[0] == 1:
                col_val = [query[1], query[2]]
                
                if col_val not in col:
                    col.append(col_val)
                    ans += query[2] * n
                    if row != []:
                        for row_index in row:
                            point = [query[1], row_index[0], row_index[1]]
                            if point not in key_point:
                                key_point.append([query[1], row_index[0], row_index[1]])
                                ans -= row_index[1]
                            elif point in key_point:
                                ans -= key_point[key_point.index(point)][2]
                                key_point[key_point.index(point)][2] = row_index[1]
                
                elif col_val in col:
                    ans += query[2] * n
                    ans -= col[col.index(col_val)][1] * n
                    for index in range(len(key_point)):
                        if key_point[index][0] == query[1]:
                            ans += col[col.index(col_val)][1]
                            ans -= key_point[index][2]
                            key_point[index][2] = col[col.index(col_val)][1]
        
        return ans
            
    
if __name__ == '__main__':
    n = 3
    queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
    print(Solution().matrixSumQueries(n, queries))