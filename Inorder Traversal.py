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

########################################################      
        
    # set up a stack for running through the tree nodes with "left - right" order
    # pop the top of the stack into the list for recording if the left and right nodes of the top were None 
    # or have been recorded in a list 
    
    def inorder_nr(self):
        
        if not self:
            return []
        
        ls = []
        stack = []
        stack.append(self)
        
        while stack:
            
            temp = stack[-1]
            
            if temp.left:
                stack.append(temp.left)
            else:
                while stack:
                    ls.append(stack.pop().val)
                    if not temp.right:
                        if stack:
                            temp = stack[-1]
                    else:
                        stack.append(temp.right) 
                        break

        return ls

########################################################    
    
    def inorder_nr_2(root):
        
        stack = []
        res = []
        
        while root or stack: # take wether root is None to get into loop
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack[-1]
                res.append(stack.pop().val)
                root = root.right
        
        return res
    
########################################################   
        
    def inorder_r(self):
        
        ls = []
        return self.inorder_r_deep([])
    
    def inorder_r_deep(self,ls):
        
        if not self:
            return []
        
        if self.left:
            self.left.inorder_r_deep(ls)
        ls += [self.val] 
        if self.right:
            self.right.inorder_r_deep(ls)
        
        
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

print(root.inorder_nr())

print(root.inorder_nr_2())

print(root.inorder_r())
