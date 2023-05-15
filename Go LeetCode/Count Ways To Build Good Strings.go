package main

const mod = 1000000007

func countGoodStrings(low int, high int, zero int, one int) int {
	memo := make(map[int]map[int]map[int]int)
	return countGoodStringsHelper(low, high, zero, one, 0, 0, memo)
}

func countGoodStringsHelper(low int, high int, zero int, one int, count int, ones int, memo map[int]map[int]map[int]int) int {
	if count > high {
		return 0
	}
	if zero == 0 && one == 0 {
		if count >= low && count <= high {
			return 1
		}
		return 0
	}
	if memo[zero] != nil && memo[zero][one] != nil && memo[zero][one][count] != 0 {
		return memo[zero][one][count]
	}
	ans := 0
	if ones == 0 {
		if zero > 0 {
			ans = (ans + countGoodStringsHelper(low, high, zero-1, one, count, 1, memo)) % mod
		}
	}
	if one > 0 {
		ans = (ans + countGoodStringsHelper(low, high, zero, one-1, count+1, 1, memo)) % mod
	}
	ans = (ans + countGoodStringsHelper(low, high, zero, one, count, 0, memo)) % mod
	if ones == 1 {
		if zero > 0 {
			ans = (ans + countGoodStringsHelper(low, high, zero-1, one, count+1, 0, memo)) % mod
		}
	}
	if memo[zero] == nil {
		memo[zero] = make(map[int]map[int]int)
	}
	if memo[zero][one] == nil {
		memo[zero][one] = make(map[int]int)
	}
	if memo[zero][one][count] == 0 {
		memo[zero][one][count] = ans
	} else {
		memo[zero][one][count] = (memo[zero][one][count] + ans) % mod
	}
	return ans
}
