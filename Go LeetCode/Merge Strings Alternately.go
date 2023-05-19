package main

import "strings"

func mergeAlternately(word1 string, word2 string) string {
	merged := make([]string, len(word1)+len(word2))
	n := 0
	if len(word1) < len(word2) {
		n = len(word1)
	} else {
		n = len(word2)
	}
	p := 0
	for i := 0; i < n; i++ {
		merged[p] = string(word1[i])
		p++
		merged[p] = string(word2[i])
		p++
	}
	if len(word1) > len(word2) {
		merged = append(merged, strings.Split(word1, "")...)
	} else {
		merged = append(merged, strings.Split(word2, "")...)
	}
	res := ""
	return strings.Join(merged, res)
}
