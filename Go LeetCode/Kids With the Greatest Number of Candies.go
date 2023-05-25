package main

func findMax(numbers *[]int) int {
	max := (*numbers)[0]
	for _, num := range *numbers {
		if num > max {
			max = num
		}
	}
	return max
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	res := make([]bool, len(candies))
	max := findMax(&candies)
	for i := 0; i < len(candies); i++ {
		if candies[i]+extraCandies >= max {
			res[i] = true
		}
	}
	return res
}
