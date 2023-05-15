package main

import (
	"sort"
)

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func maxScore(nums []int) int {
	maxValues := []int{}
	sort.Ints(nums)
	n := len(nums) / 2
	tmp := 0
	res := 0
	remove_idx := 0
	for i := len(nums) - 1; i > -1; i-- {
		if nums[i] == 0 {
			continue
		}
		tmp = 0
		for j := i - 1; j > -1; j-- {
			if nums[j] == 0 {
				continue
			}
			if nums[j] < tmp {
				break
			}
			a := gcd(nums[j], nums[i])
			if a >= tmp {
				tmp = a
				remove_idx = j
			}
		}
		nums[i] = 0
		nums[remove_idx] = 0
		maxValues = append(maxValues, tmp)

	}

	sort.Ints(maxValues)

	for k := 1; k <= n; k++ {
		res += k * maxValues[k-1]
	}
	return res
}

func main() {
	println(maxScore([]int{3, 4, 6, 8}))                     // 11
	println(maxScore([]int{1, 2, 3, 4, 5, 6}))               // 14
	println(maxScore([]int{3, 5, 9, 15}))                    // 14
	println(maxScore([]int{697035, 181412, 384958, 575458})) // 869
}
