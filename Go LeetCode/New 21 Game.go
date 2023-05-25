package main

func new21Game(n int, k int, maxPts int) float64 {
	if k == 0 {
		return 1.0
	}
	if n >= k-1+maxPts {
		return 1.0
	}

	dp := make([]float64, n+1)
	var res float64
	win := 1.0

	dp[0] = 1.0
	for i := 1; i <= n; i++ {
		dp[i] = win / float64(maxPts)
		if i < k {
			win += dp[i]
		} else {
			res += dp[i]
		}
		if i >= maxPts {
			win -= dp[i-maxPts]
		}
	}
	return res
}
