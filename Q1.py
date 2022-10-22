# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def Findmid(head):
            if not head:
                return None
            previous = None
            fast, slow = head, head
            while fast and fast.next:
                previous = slow
                slow = slow.next
                fast = fast.next.next

            if previous:
                previous.next = None

            return slow

        if not head:
            return None

        mid = Findmid(head)
        node = TreeNode(val = mid.val)

        if mid == head:
            return node


        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node

