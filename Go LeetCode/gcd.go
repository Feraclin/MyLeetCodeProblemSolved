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

func main() {
	println(gcd(384958, 575458))
	println(gcd(697035, 181412))
	println(gcd(697035, 575458))
	println(gcd(384958, 181412))
}
