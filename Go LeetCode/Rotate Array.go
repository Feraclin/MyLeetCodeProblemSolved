package main

import "fmt"

//func rotate(nums []int, k int) {
//	n := len(nums)
//	k %= n
//	reverse(nums[:n-k])
//	reverse(nums[n-k:])
//	reverse(nums)
//}
//func reverse(nums []int) {
//	for i, n := 0, len(nums); i < n/2; i++ {
//		nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
//	}
//}

func rotate(nums []int, k int) {
	m := len(nums) - k
	newNums := append(nums[m:], nums[:m]...)
	for i, n := range newNums {
		nums[i] = n
	}
}

func main() {
	rotate([]int{1, 2, 3, 4, 5, 6, 7}, 3)
	x := func(fn func(i int) int, i int) func(int) int { return fn }(func(i int) int { return i + 1 }, 5)
	fmt.Printf("%L", x)
}
