class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        stack = [[0]]
        
        ans = []
        
        while(stack):
            
            p = stack.pop()
            
            for i in graph[p[-1]]:
                
                if(i == len(graph)-1):
                    ans.append(p + [i])
                
                else:
                    stack.append(p + [i])
        
        return ans