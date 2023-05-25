package main

func largestAltitude(gain []int) int {
	var tmp, max int
	for _, n := range gain {
		tmp += n
		if tmp > max {
			max = tmp
		}
	}
	return max
}
