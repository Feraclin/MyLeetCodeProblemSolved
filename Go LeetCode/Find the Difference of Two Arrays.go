package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	nums1Map := make(map[int]bool)
	nums2Map := make(map[int]bool)

	for _, num := range nums1 {
		nums1Map[num] = true
	}
	for _, num := range nums2 {
		nums2Map[num] = true
	}

	nums1Only := []int{}
	nums2Only := []int{}

	for num := range nums1Map {
		if !nums2Map[num] {
			nums1Only = append(nums1Only, num)
		}
	}

	for num := range nums2Map {
		if !nums1Map[num] {
			nums2Only = append(nums2Only, num)
		}
	}

	return [][]int{nums1Only, nums2Only}
}
