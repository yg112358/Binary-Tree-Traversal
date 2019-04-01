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
    # pop the top of the stack into the list for recording and push its nodes into the stack
    
    def preorder_nr(self):
      
        stack = []
        ls = []

        temp = root

        stack.append(temp)

        while stack:
            ls.append(stack.pop().val)

            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

            if stack:
                temp = stack[-1]   

        return ls
    
    
    def preorder_r(self):
        
        ls = []
        return self.preorder_r_deep([])
    
    def preorder_r_deep(self,ls):
        
        if self is None:
            return []
        
        ls += [self.val] 
        if self.left:
            self.left.preorder_r_deep(ls)
        if self.right:
            self.right.preorder_r_deep(ls)
        
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

print(root.preorder_nr())

print(root.preorder_r())