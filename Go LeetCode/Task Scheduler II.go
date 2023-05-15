package main

func taskSchedulerII(tasks []int, space int) int64 {
	var daysLeft int64
	taskMap := make(map[int]int)
	for i, t := range tasks {
		if taskMap[t] == 0 {
			taskMap[t] = i
			daysLeft++
		} else {

		}

	}
	return daysLeft
}
