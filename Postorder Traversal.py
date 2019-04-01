class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def trace(self):
        
        ls = []
        return self.trace_deep([])

    def trace_deep(self,ls):
        
        tl=[]
        ls.append(self.val)
        lsclone = [x for x in ls]
    
        
        if self.left:           
            tl = tl + self.left.trace_deep(ls)
            
        if self.right:            
            tl = tl + self.right.trace_deep(ls) 

        if self.left == None and self.right == None:
            tl.append(lsclone)
        
        ls.pop()
      
        return tl

    # set up a stack for running through the tree nodes with "left - right" order
    # pop the top of the stack into the list for recording if the left and right nodes of the top were None 
    # or have been recorded in a list 
    
    def postorder_nr(self):
        
        ls = []
        stack = []
        
        stack.append(self)
        while stack:
            
            temp = stack[-1]
            
            if not temp.left and not temp.right:
                ls.append(stack.pop())
                continue
            if ls and (temp.left is ls[-1] or temp.right is ls[-1]): # only check ls[-1] for minimizing time comlexity 
                ls.append(stack.pop())
                continue
      
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
                
        ls = [x.val for x in ls]
        
        return ls

    
    
    def postorder_r(self):
        
        ls = []
        return self.postorder_r_deep([])
    
    def postorder_r_deep(self,ls):
        
        if self is None:
            return []
        
        if self.left:
            self.left.postorder_r_deep(ls)
        if self.right:
            self.right.postorder_r_deep(ls)
        ls += [self.val] 
        
        return ls
        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)


# Input:

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#    /       \
#   8         9


print(root.trace())

print(root.postorder_nr())

print(root.postorder_r())
