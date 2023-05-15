package main

func spiralOrder(matrix [][]int) []int {
	var array []int
	recurseSpiral(matrix, &array, 0, 0)
	return array
}

func recurseSpiral(matrix [][]int, array *[]int, i, j int) {
	if i >= 0 && j >= 0 && i < len(matrix) && j < len(matrix[0]) && matrix[i][j] != -999999 {
		*array = append(*array, matrix[i][j])
		matrix[i][j] = -999999
		if i == 0 || matrix[i-1][j] == -999999 {
			recurseSpiral(matrix, array, i, j+1)
		}
		recurseSpiral(matrix, array, i+1, j)
		recurseSpiral(matrix, array, i, j-1)
		recurseSpiral(matrix, array, i-1, j)
	}
}
