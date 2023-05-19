package main

func checkNode(graph *[][]int, statusLst *[]int, node, status int) bool {
	if (*statusLst)[node] != 0 {
		return (*statusLst)[node] == status
	}
	(*statusLst)[node] = status
	for _, v := range (*graph)[node] {
		if !checkNode(graph, statusLst, v, -status) {
			return false
		}
	}
	return true
}

func isBipartite(graph [][]int) bool {
	statusLst := make([]int, len(graph))
	for node, _ := range graph {
		if statusLst[node] == 0 && !checkNode(&graph, &statusLst, node, 1) {
			return false
		}
	}
	return true
}
