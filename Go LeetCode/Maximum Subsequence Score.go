package main

import (
	"fmt"
	"sort"
)

func checkRes(keys *[]int, dictionary *map[int]int, num int, i int, k int) {
	if len(*keys) >= k && num > (*dictionary)[(*keys)[len(*keys)-1]] {
		*keys = append((*keys)[:len(*keys)-1], i)
	} else {
		*keys = append((*keys), i)
	}
	sort.Slice(*keys, func(i, j int) bool {
		return (*dictionary)[(*keys)[i]] > (*dictionary)[(*keys)[j]]
	})
}

func score(nums1 []int, nums2 []int, k int) int64 {
	var res int64 = 0
	var scores []int
	scoreLst := make(map[int]int, len(nums1))
	for i := 0; i < len(nums1); i++ {
		scoreLst[i] = nums1[i] * nums2[i]
		checkRes(&scores, &scoreLst, nums1[i]*nums2[i], i, k)
	}
	var left, right int
	fmt.Println(scores)
	fmt.Println(scoreLst)
	right = nums2[scores[0]]
	for i := 0; i < k; i++ {
		left += nums1[scores[i]]
		if nums2[scores[i]] < right {
			right = nums2[scores[i]]
		}
	}
	res = int64(left) * int64(right)
	return res
}

func main() {
	println(score([]int{1, 3, 3, 2}, []int{2, 1, 3, 4}, 3))
}
