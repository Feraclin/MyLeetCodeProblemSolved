package main

func gcdOfStrings(s1 string, s2 string) string {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	if s1+s2 != s2+s1 {
		return ""
	}
	x := gcd(len(s1), len(s2))
	return s1[:x]

}
