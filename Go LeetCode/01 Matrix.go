package main

func checkNearest(mat *[][]int, x int, y int) int {
	a, b, c, d := 10000, 10000, 10000, 10000
	if x > 0 {
		a = (*mat)[x-1][y]
	}
	if y > 0 {
		b = (*mat)[x][y-1]
	}
	if x < len(*mat)-1 {
		c = (*mat)[x+1][y]
	}
	if y < len((*mat)[0])-1 {
		d = (*mat)[x][y+1]
	}
	return min(a, min(b, min(c, d)))
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func updateMatrix(mat [][]int) [][]int {
	n, m := len(mat), len(mat[0])
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] != 0 {
				mat[i][j] += checkNearest(&mat, i, j)
			}
		}
	}
	return mat
}
