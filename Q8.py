class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(node):
            nonlocal result
            if not node:
                return 0
            if low <= node.val <= high:
                result += node.val
            if node.val > low:
                inorder(node.left)
            if node.val < high:
                inorder(node.right)

        result = 0
        inorder(root)
        return result

        