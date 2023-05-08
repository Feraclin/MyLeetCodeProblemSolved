package main

import "fmt"

func search(nums []int, target int) int {
	left, right := 0, len(nums)-1
	mid := len(nums) / 2
	for {
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
		mid = (left + right) / 2
		if left > right {
			return -1
		}
	}
	return mid
}

func main() {
	fmt.Println(search([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}, 10))
}
