class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            start = head.next
        else:
            start = head
        while head and head.next:

            body = head.next

            if body.next:
                tail = body.next
            else:
                tail = None

            body.next = head
            head.next = tail

            head, tail = tail, head

            if head and head.next:
                tail.next = head.next
            else:
                tail.next = head
        return start