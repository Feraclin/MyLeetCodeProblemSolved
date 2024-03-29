package main

type ListNode struct {
	Val  int
	Next *ListNode
}

type Node struct {
	Val      int
	Left     *Node
	Right    *Node
	Next     *Node
	Children []*Node
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
