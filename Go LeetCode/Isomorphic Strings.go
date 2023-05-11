package main

import "fmt"

func isIsomorphic(s string, t string) bool {
	table := make(map[byte]byte)
	unique := make(map[byte]bool)
	for i := 0; i < len(s); i++ {
		if _, ex := unique[t[i]]; !ex && table[s[i]] == 0 {
			table[s[i]] = t[i]
			unique[t[i]] = true
		} else {
			if table[s[i]] == t[i] {
				continue
			} else {
				return false
			}

		}
	}
	return true
}

func main() {
	fmt.Println(isIsomorphic("egg", "add"))
	fmt.Println(isIsomorphic("foo", "bar"))
	fmt.Println(isIsomorphic("paper", "title"))
}
