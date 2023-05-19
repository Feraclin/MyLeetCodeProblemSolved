package main

func moveZeroes(nums []int) {
	num := 0
	for i, c := range nums {
		if c == 0 {
			num++
		} else {
			nums[i-num] = c
		}
	}
	for i := len(nums) - num; i < len(nums); i++ {
		nums[i] = 0
	}
}
