class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]):
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        graph_cp = graph.copy()
            
        for edge in edges:
            graph[edge[0]].remove(edge[1])
            graph[edge[1]].remove(edge[0])
            
            q0 = []
            q1 = []
            
            
            while True:
                
                q0 += graph[edge[0]]
                q1 += graph[edge[1]]
                
                
    

if __name__ == '__main__':
    pass