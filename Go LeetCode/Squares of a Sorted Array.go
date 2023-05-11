package main

import "sort"

func sortedSquares(nums []int) []int {
	for k, v := range nums {
		nums[k] = v * v
	}
	sort.Ints(nums)
	return nums
}
