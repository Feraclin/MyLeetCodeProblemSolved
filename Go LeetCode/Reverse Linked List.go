package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	var lst []*ListNode
	if head == nil {
		return nil
	}
	for {
		lst = append(lst, head)
		if head.Next == nil {
			break
		}
		head = head.Next
	}
	if len(lst) == 0 {
		return nil
	}
	for i := len(lst) - 1; i > 0; i-- {
		lst[i].Next = lst[i-1]
	}
	lst[0].Next = nil
	return lst[len(lst)-1]
}
