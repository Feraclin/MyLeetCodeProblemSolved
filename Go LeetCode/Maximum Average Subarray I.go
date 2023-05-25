package main

import "fmt"

func findMaxAverage(nums []int, k int) float64 {
	var tmp float64
	for i := 0; i < k; i++ {
		tmp += float64(nums[i])
	}
	max := tmp
	for i, j := 0, k; j < len(nums); i, j = i+1, j+1 {
		tmp -= float64(nums[i])
		tmp += float64(nums[j])
		if tmp > max {
			max = tmp
		}
	}
	return max / float64(k)
}

func main() {
	fmt.Println(findMaxAverage([]int{1, 12, -5, -6, 50, 3}, 4))

}
