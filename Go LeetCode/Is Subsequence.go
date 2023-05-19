package main

func isSubsequence(s string, t string) bool {
	n := 0
	if len(s) == 0 {
		return true
	}
	for i := 0; i < len(t); i++ {
		if t[i] == s[n] {
			n++
		}
		if n >= len(s) {
			return true
		}
	}
	return false
}
