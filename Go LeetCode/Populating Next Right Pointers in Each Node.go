package main

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}

	// Установка связи между левым и правым дочерними узлами текущего узла
	if root.Left != nil {
		root.Left.Next = root.Right
	}

	// Установка связи между правым дочерним узлом текущего узла и левым дочерним узлом его соседнего узла
	if root.Right != nil && root.Next != nil {
		root.Right.Next = root.Next.Left
	}

	// Рекурсивный вызов функции connect для левого и правого дочерних узлов текущего узла
	connect(root.Left)
	connect(root.Right)

	return root
}
