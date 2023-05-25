package main

import "fmt"

func tribonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n < 3 {
		return 1
	}

	a, b, c := 0, 1, 1
	for i := 3; i <= n; i++ {
		a, b, c = b, c, a+b+c
	}

	return c
}

func main() {
	// Example usage
	n := 4
	result := tribonacci(n)
	fmt.Printf("Tribonacci number T%d: %d\n", n, result)
}
