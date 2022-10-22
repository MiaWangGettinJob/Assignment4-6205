class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def findswap(node):
            nonlocal x, y, last
            if not node:
                return

            findswap(node.left)

            if node.val < last.val:
                if not y:
                    y = last
                    x = node
                else:
                    x = node
                    return
            last = node

            findswap(node.right)

            x, y, last= None, None, TreeNode(val = float("-inf"))
            findswap(root)
            y.val, x.val = x.val, y.val