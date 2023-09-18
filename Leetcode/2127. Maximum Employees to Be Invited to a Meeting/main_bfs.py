import numpy as np

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        
        indeg = np.zeros(n)
        used = np.zeros(n)
        line = np.zeros(n)
        
        for i in range(n):
            indeg[favorite[i]] += 1
            
        q = []
        
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                

        while q:
            
            node = q[0]
            used[node] = 1
            
            q.pop(0)
            
            next_node = favorite[node]
            
            line[next_node] = max(line[node] + 1, line[next_node])
            
            indeg[next_node] -= 1
            
            if indeg[next_node] == 0:
                q.append(next_node)
                
        ring = 0
        total = 0
        
        for i in range(n):
            if used[i] == 0:
                
                next_node = favorite[i]
                
                if favorite[next_node] == i:
                    
                    total += line[next_node] + line[i] + 2
                    
                    used[next_node] = 1
                    
                else:
                    tmp_ring = 0
                    
                    while(used[next_node] == 0):
                        
                        tmp_ring += 1
                        used[next_node] = 1
                        next_node = favorite[next_node]

                    ring = max(ring, tmp_ring)
                    
        return int(max(total, ring))
                    
        
        
             


if __name__ == '__main__':
    
    favorite = [1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]
    
    s = Solution()
    
    print(s.maximumInvitations(favorite))    