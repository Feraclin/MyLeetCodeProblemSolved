package main

import "fmt"

func predictPartyVictory(senate string) string {
	queue := []byte(senate)
	var banD, banR int
	return voteTour(queue, banD, banR)
}

func voteTour(queue []byte, voteD, voteR int) string {
	var countR, countD int
	queue1 := []byte{}
	for _, v := range queue {
		switch v {
		case 'R':
			if voteR > 0 {
				voteR--
			} else {
				voteD++
				countR++
				queue1 = append(queue1, 'R')
			}
		case 'D':
			if voteD > 0 {
				voteD--
			} else {
				voteR++
				countD++
				queue1 = append(queue1, 'D')
			}
		}
	}
	if countR == 0 {
		return "Dire"
	}
	if countD == 0 {
		return "Radiant"
	}
	return voteTour(queue1, voteD, voteR)
}

func main() {
	fmt.Println(predictPartyVictory("RD"))
	fmt.Println(predictPartyVictory("RDD"))
	fmt.Println(predictPartyVictory("RRDDD"))
	fmt.Println(predictPartyVictory("DRRDRDRDRDDRDRDR")) // Radiant
}
