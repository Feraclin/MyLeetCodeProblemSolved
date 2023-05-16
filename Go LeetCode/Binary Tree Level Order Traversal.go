package main

func levelOrder(root *TreeNode) [][]int {
	var res [][]int
	var add func(root *TreeNode, list *[][]int) int
	add = func(root *TreeNode, list *[][]int) int {
		if root != nil {
			left := add(root.Left, list)
			right := add(root.Right, list)
			*list = append(*list, []int{left, right})
			return root.Val
		}
		return 0
	}
	res = append(res, []int{add(root, &res)})
	return res

