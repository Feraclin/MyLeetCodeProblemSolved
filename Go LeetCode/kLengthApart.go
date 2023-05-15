package main

func kLengthApart(nums []int, k int) bool {
	away := k
	for _, c := range nums {
		if c == 0 {
			away++
			continue
		}
		if c == 1 && away >= k {
			away = 0
		} else {
			return false
		}
	}
	return true
}
