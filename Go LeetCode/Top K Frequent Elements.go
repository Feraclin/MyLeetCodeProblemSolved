package main

import "sort"

func sortDictionary(dictionary *map[int]int, values []int) []int {
	keys := make([]int, 0, len(*dictionary))

	for key := range *dictionary {
		keys = append(keys, key)
	}

	sort.Slice(keys, func(i, j int) bool {
		return (*dictionary)[keys[i]] > (*dictionary)[keys[j]]
	})

	for _, key := range keys {
		if (*dictionary)[key] > values[len(values)-1] {
			values[len(values)-1] = (*dictionary)[key]
			sort.Sort(sort.Reverse(sort.IntSlice(values)))
		}
	}

	sortedKeys := keys[:len(values)]
	return sortedKeys
}

func topKFrequent(nums []int, k int) []int {
	m := map[int]int{}
	for _, num := range nums {
		m[num]++
	}
	return sortDictionary(&m, make([]int, k))
}
