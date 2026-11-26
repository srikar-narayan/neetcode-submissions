# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #height of children combined = diamater of a node
        # recursive DFS

        def dfs(root):
            if root == None:
                return (0, 0)
            leftH, leftD = dfs(root.left)
            rightH, rightD = dfs(root.right)

            height = 1 + max(leftH, rightH)
            diameter = max(leftH + rightH, leftD, rightD)
            return (height, diameter)
        
        return dfs(root)[1]
            

        