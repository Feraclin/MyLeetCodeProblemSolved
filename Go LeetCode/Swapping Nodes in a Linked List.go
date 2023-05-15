package main

func swapNodes(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var p, q, tmp *ListNode
	p = head
	q = head
	tmp = head
	for i := 0; tmp != nil; i++ {
		tmp = tmp.Next
		if i+1 < k {
			q = q.Next
		}
		if i >= k {
			p = p.Next
		}
	}
	q.Val, p.Val = p.Val, q.Val
	return head
}
