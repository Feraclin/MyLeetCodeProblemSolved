package main

import "fmt"

func changeColor(image [][]int, sr int, sc int, oldColor int, newColor int) {
	if image[sr][sc] != oldColor {
		return
	} else {
		image[sr][sc] = newColor
	}
	if sr > 0 {
		changeColor(image, sr-1, sc, oldColor, newColor)
	}
	if sc < len(image[0])-1 {
		changeColor(image, sr, sc+1, oldColor, newColor)
	}
	if sc > 0 {
		changeColor(image, sr, sc-1, oldColor, newColor)
	}
	if sr < len(image)-1 {
		changeColor(image, sr+1, sc, oldColor, newColor)
	}
}

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	if image[sr][sc] != color {
		changeColor(image, sr, sc, image[sr][sc], color)
	}
	return image
}

func main() {
	image := [][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}
	sr := 1
	sc := 1
	color := 2
	// Output: [[2,2,2],[2,2,0],[2,0,1]]
	fmt.Println(floodFill(image, sr, sc, color))
	image = [][]int{{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
	color = 0
	fmt.Println(floodFill(image, sr, sc, color))
}
