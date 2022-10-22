class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        """
        def helper(root):
            return [root.val] + helper(root.left) + helper(root.right) if root else []

        List = helper(root)
        return ' '.join(map(str,List))



    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def helper(low = float("-inf") , high = float("inf")):
            nonlocal index
            if index == n:
                return None

            value = int(data[index])
            if value > high or value < low:
                return None

            index += 1
            node = TreeNode(value)
            node.left = helper(low, value)
            node.right = helper(value, high)
            return node

        index = 0
        data = data.split()
        n = len(data)
        return helper()
