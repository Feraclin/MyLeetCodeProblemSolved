package main

import "fmt"

func checkArea(image [][]int, sr int, sc int) int {
	n := 0
	if image[sr][sc] != 1 {
		return n
	} else {
		image[sr][sc] = 2
		n += 1
	}
	if sr > 0 {
		n += checkArea(image, sr-1, sc)
	}
	if sc < len(image[0])-1 {
		n += checkArea(image, sr, sc+1)
	}
	if sc > 0 {
		n += checkArea(image, sr, sc-1)
	}
	if sr < len(image)-1 {
		n += checkArea(image, sr+1, sc)
	}
	return n
}

func maxAreaOfIsland(grid [][]int) int {
	max, n := 0, 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				n = checkArea(grid, i, j)
				if n > max {
					max = n
				}
			}
		}
	}
	return max
}

func main() {
	image := [][]int{{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}}
	fmt.Println(maxAreaOfIsland(image))
}
