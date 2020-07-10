"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        
        if(head is None):
            return None
        
        def depth(curr,pending):
            
            while(curr is not None):

                if(curr.child):
                    pending.append(curr.next)
                    if(curr.next is not None):
                        temp = curr.child
                        curr.child = None
                        curr.next = temp
                        temp.prev = curr
                        
                prev = curr
                curr = curr.next
        
            curr = prev
            
            
            while(pending):
                p = pending.pop()
                curr.next = p
                p.prev = curr
                dfs(curr,pending)
        
        depth(head,[])
        
        

        
        return head
        
        


            
            