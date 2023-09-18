import numpy as np

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        self.n = len(favorite)
        self.graph = favorite
        
        # graph recording indegree
        for i in range(self.n):
            self.graph[i] = favorite[i]
            
        self.mark = np.zeros(self.n)
        self.node_list = []
        self.circle_info = []
        
        for i in range(self.n):
            self.visit(i)
            self.mark = np.zeros(self.n)
            self.node_list = []
                
                
        print(self.circle_info)
        
        self.circle_simplify()
        
        self.ans.append(sum(self.circle_cp))
        
        print(self.circle_cp)
        print(self.ans)
        
        return max(self.ans)
               

            
    def visit(self, node):
        
        if self.mark[node] == 1:
            self.node_list.append(node)
            circle_num = self.check_circle_num(node)            
            self.circle_info.append([circle_num, len(self.node_list) - 1, []])
            if circle_num == 2:
                self.circle_info[-1][-1] = [node, self.node_list[-2]]
            
            return
            
        self.mark[node] = 1
        self.node_list.append(node)
        
        self.visit(self.graph[node])
            
    def check_circle_num(self, num):
        
        first_index = self.node_list.index(num)
        
        return len(self.node_list) - first_index - 1
    
    def circle_simplify(self):
        self.circle_info_simplify = {}
        self.circle_cp = []
        self.ans = []
        
        for i in range(len(self.circle_info)):
            if str(self.circle_info[i][-1]) not in self.circle_info_simplify:
                self.circle_info_simplify[str(self.circle_info[i][-1])] = self.circle_info[i][0:2]
                
            else:
                if str(self.circle_info[i][-1]) != '[]':
                    if self.circle_info[i][1] > self.circle_info_simplify[str(self.circle_info[i][-1])][1]:
                        self.circle_info_simplify[str(self.circle_info[i][-1])] = self.circle_info[i][0:2]
                else:
                    if self.circle_info[i][0] > self.circle_info_simplify[str(self.circle_info[i][-1])][0]:
                        self.circle_info_simplify[str(self.circle_info[i][-1])] = self.circle_info[i][0:2]
                    
        
        print(self.circle_info_simplify)
    
        items = list(self.circle_info_simplify.items())
        
        while len(items) != 0:
            key, val = items[0]
            
            if key == '[]':
                self.ans.append(val[0])
                items.pop(0)
                
            key = key[1:-1]
            key = key.split(',')[0]
                
            for i in range(1, len(items)):
                if items[i][0] != '[]':
                    key_cp = items[i][0][1:-1].split(',')[1][1:]
                    
                    if key == key_cp:
                        self.circle_cp.append(val[1] + items[i][1][1] - 2)
                        
                        items.pop(i)
                        items.pop(0)
                        
                        break
                    
if __name__ == '__main__':
    favorite = [6,10,10,0,6,0,4,4,1,3,3]
    
    s = Solution()
    
    print(s.maximumInvitations(favorite))