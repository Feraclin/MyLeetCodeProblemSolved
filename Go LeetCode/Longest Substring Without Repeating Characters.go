package main

func lengthOfLongestSubstring(s string) int {
	if len(s) < 2 {
		return len(s)
	}
	var max int
	map_map := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		if j, ok := map_map[s[i]]; ok && max < i-j {
			max = i - j
		}
		map_map[s[i]] = i
	}
	return max
}

func main() {
	s := "abcabcbb"
	max := lengthOfLongestSubstring(s)
	println(max)
	s = "aab"
	max = lengthOfLongestSubstring(s)
	println(max)
}
