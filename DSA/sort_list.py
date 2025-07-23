# Problem: Sort List (Linked List)
# Aim: Sort a singly linked list in O(n log n) time and constant space complexity.
# Approach: Use Merge Sort, which is well-suited for linked lists.
# - Find the middle of the list using slow and fast pointers.
# - Recursively divide the list into halves.
# - Merge the sorted halves back together using a helper function.


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        mid = self.getMiddle(head)
        right = mid.next
        mid.next = None

        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)

        return self.merge(left_sorted, right_sorted)

    def getMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
