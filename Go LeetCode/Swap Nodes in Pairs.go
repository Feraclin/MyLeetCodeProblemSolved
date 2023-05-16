package main

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var start, tail, body *ListNode
	if head != nil && head.Next != nil {
		start = head.Next
	} else {
		start = head
	}
	for head != nil && head.Next != nil {
		body = head.Next
		if body.Next != nil {
			tail = body.Next
		} else {
			tail = nil
		}

		body.Next = head
		head.Next = tail

		head, tail = tail, head

		if head != nil && head.Next != nil {
			tail.Next = head.Next
		} else {
			tail.Next = head
		}
	}
	return start
}

func swapPairs2(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	node := head.Next
	head.Next = swapPairs2(node.Next)
	node.Next = head
	return node
}
