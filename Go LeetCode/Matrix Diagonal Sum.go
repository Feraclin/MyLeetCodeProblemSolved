package main

import "fmt"

func diagonalSum(mat [][]int) int {
	n := len(mat)
	res := 0
	for i := 0; i < n; i++ {
		res += mat[i][i]
		res += mat[n-1-i][i]
	}
	if n%2 == 1 {
		res -= mat[n/2][n/2]
	}
	return res
}

func main() {
	fmt.Println(diagonalSum([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
	fmt.Println(diagonalSum([][]int{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}))
	fmt.Println(diagonalSum([][]int{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}))

}
