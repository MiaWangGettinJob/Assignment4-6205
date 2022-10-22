# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validate(node, low = -math.inf, high = math.inf):

            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False
            else:
                return validate(node.left, low , node.val) and validate(node.right, node.val, high)


        return validate(root)