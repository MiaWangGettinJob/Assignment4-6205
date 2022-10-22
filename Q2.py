class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal first, last
            if not node:
                return
            helper(node.left)
            if last:
                last.right = node
                node.left = last
            if not first:
                first = node
            last = node
            helper(node.right)

        first, last = None, None
        helper(root)
        if not root:
            return None
        first.left = last
        last.right = first

        return first

                