package main

func preorder(root *Node) []int {
	var res []int

	var add func(root *Node, list *[]int)
	add = func(root *Node, list *[]int) {
		if root == nil {

			*list = append(*list, root.Val)
			for _, i := range root.Children {
				add(i, list)
			}
		}
	}
	add(root, &res)
	return res
}
