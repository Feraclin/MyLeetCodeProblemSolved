package main

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	maxProfit := 0
	minPrice := prices[0]
	for _, price := range prices {
		if price < minPrice {
			minPrice = price
		} else if price-minPrice > maxProfit {
			maxProfit = price - minPrice
		}
	}
	return maxProfit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	println(maxProfit(prices))
	prices = []int{7, 6, 5, 4}
	println(maxProfit(prices))
}
