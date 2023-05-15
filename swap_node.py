from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            start = head.next
        else:
            start = head
        while head:

            tail = None
            if not head.next:
                break
            body = head.next

            if body.next:
                tail = body.next

            body.next = head
            head.next = tail

            head, tail = tail, head

            if head and head.next:
                tail.next = head.next
            else:
                tail.next = head

        return start


s = Solution()
heads = ListNode(1, ListNode(2, ListNode(3)))
tmp = heads
while True:
    print(tmp.val)
    tmp = tmp.next
    if not tmp.next:
        break
print(tmp.val)
print('___________')
tmp = s.swapPairs(heads)
while tmp.next:
    print(tmp.val)
    tmp = tmp.next
    if not tmp.next:
        break
print(tmp.val)