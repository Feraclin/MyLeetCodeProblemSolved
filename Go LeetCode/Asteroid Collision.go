package main

import "fmt"

func asteroidCollision(asteroids []int) []int {
	res := make([]int, 0, len(asteroids))
	for _, a := range asteroids {
		for len(res) > 0 && res[len(res)-1] > 0 && a < 0 && res[len(res)-1] < -a {
			res = res[:len(res)-1]
		}
		if len(res) == 0 || a > 0 || res[len(res)-1] < 0 {
			res = append(res, a)
		} else if a < 0 && res[len(res)-1] == -a {
			res = res[:len(res)-1]
		}
	}
	return res
}

//func asteroidCollision(asteroids []int) []int {
//
//	checkMass := func(res *[]int, a *int) bool {
//		if len(*res) == 0 {
//			return true
//		}
//		switch {
//		case *a > 0 && (*res)[len(*res)-1] > 0:
//			fallthrough
//		case *a < 0 && (*res)[len(*res)-1] < 0:
//			return true
//		}
//		return false
//	}
//
//	res := make([]int, 0, len(asteroids))
//	for _, a := range asteroids {
//		if len(res) == 0 {
//			res = append(res, a)
//			continue
//		}
//		if checkMass(&res, &a) {
//			res = append(res, a)
//			continue
//
//		} else {
//
//			for {
//				if checkMass(&res, &a) {
//					break
//				} else if a*-1 > res[len(res)-1] {
//					res = res[:len(res)-1]
//				} else if a*-1 == res[len(res)-1] {
//					res = res[:len(res)-1]
//				} else {
//					break
//				}
//			}
//		}
//	}
//	return res
//}

func main() {
	fmt.Println(asteroidCollision([]int{5, 10, -5}))
	fmt.Println(asteroidCollision([]int{8, -8}))
	fmt.Println(asteroidCollision([]int{10, 2, -5}))
}
