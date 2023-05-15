package main

func longestPalindrome(s string) int {
	seen := make([]bool, 58)
	length := 0

	for _, char := range s {
		if seen[int(char-'A')] {
			seen[int(char-'A')] = false
			length += 2
			continue
		}
		seen[int(char-'A')] = true
	}

	if len(s) > length {
		length++
	}

	return length
}
