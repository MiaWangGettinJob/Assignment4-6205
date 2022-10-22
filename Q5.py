class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorderList = self.inorder(root)
        self.pointer = -1


    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []



    def next(self) -> int:
        self.pointer += 1
        return self.inorderList[self.pointer]


    def hasNext(self) -> bool:
        if self.pointer < len(self.inorderList) - 1:
            return True
        else:
            return False
