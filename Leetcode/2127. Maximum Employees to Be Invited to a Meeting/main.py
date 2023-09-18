import numpy as np

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        self.n = len(favorite)
        self.graph = [[] for _ in range(self.n)]
        
        # graph recording indegree
        for i in range(self.n):
            self.graph[favorite[i]].append(i)
            
        return self.check_circle()
    
    def check_circle(self):
        
        ans = []
        self.line = 0
        self.max_line_circle = 0
        
        for i in range(self.n):
            
            self.mark = np.zeros(self.n)
            self.circle = []
            self.visit(i)
            if self.circle:
                ans.append(max(self.circle))                   
        
        
        ans.append(self.max_line_circle + self.line - 2)
        
        return int(max(ans)) 
            
    def visit(self, n):
        
        if self.mark[n] == 1:
            mark_copy = self.mark.copy()
            circle_num = self.mark.sum()
            if circle_num == 2:
                self.line += 1
                circle_num = self.expand()
                self.mark = mark_copy
            self.circle.append(circle_num)
        
            return
        
        self.mark[n] = 1
        
        for node in self.graph[n]:
            self.visit(node)
            
        self.mark[n] = 0
        
    def expand(self):
        indices = np.where(self.mark == 1)[0]
        
        ans = 2
        for index in indices:
            node_list = []
            
            for node in self.graph[index]:
                if self.mark[node] == 0:
                    self.mark[node] = 1
                    node_list.append(node)
            
            
            while True:
                if not node_list:
                    break
                
                next_node_list = node_list.copy()
                node_list = []
                
                ans += 1
                
                for node in next_node_list:
                    for next_node in self.graph[node]:
                        if self.mark[next_node] == 0:
                            self.mark[next_node] = 1
                            node_list.append(next_node)
                            
                
        if ans > self.max_line_circle:
            self.max_line_circle = ans
                            
        return ans
        
    
    
if __name__ == '__main__':
    favorite = [1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]
    
    s = Solution()
    
    print(s.maximumInvitations(favorite))
            