package main

func gcd(a int, b int) int {
	if b > a {
		a, b = b, a
	}
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}
