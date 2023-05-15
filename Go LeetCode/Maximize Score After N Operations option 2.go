package main

func gcd(a, b int) int {
	if a < b {
		a, b = b, a
	}
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func gcds(nums []int) [][]int {
	n := len(nums)
	b := make([][]int, n)
	for i := 0; i < n; i++ {
		b[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			curGcd := gcd(nums[i], nums[j])
			b[i][j] = curGcd
			b[j][i] = curGcd
		}
	}

	return b
}

// Функция для нахождения максимальной суммы наибольших общих делителей
func maxScore(nums []int) int {
	n := len(nums)
	memo := make(map[int]int) // Создаем карту для хранения результатов вычислений

	b := gcds(nums) // Находим все наибольшие общие делители между парами чисел из массива

	var dfs func(pos int, mask int) int // Объявляем функцию dfs для рекурсивного поиска максимальной суммы наибольших общих делителей
	dfs = func(pos int, mask int) int { // Функция dfs принимает на вход позицию и маску
		if pos > n/2 { // Если позиция больше, чем половина длины массива, возвращаем 0
			return 0
		}
		if v, ok := memo[mask]; ok { // Если результат уже есть в карте, возвращаем его
			return v
		}
		res := 0                 // Инициализируем переменную для хранения максимальной суммы
		for i := 0; i < n; i++ { // Проходимся по всем парам чисел из массива
			for j := i + 1; j < n; j++ {
				newMask := (1 << i) | (1 << j) // Создаем новую маску, которая указывает, какие числа уже были использованы
				if mask&newMask == 0 {         // Если числа еще не использовались
					sum := pos*b[i][j] + dfs(pos+1, newMask|mask) // Вычисляем сумму и рекурсивно вызываем функцию для следующей позиции
					if sum > res {                                // Если сумма больше максимальной, обновляем ее
						res = sum
					}
				}
			}
		}

		memo[mask] = res // Сохраняем результат в карте
		return res
	}
	return dfs(1, 0)
}

func main() {
	println(maxScore([]int{3, 4, 6, 8}))                     // 11
	println(maxScore([]int{1, 2, 3, 4, 5, 6}))               // 14
	println(maxScore([]int{3, 5, 9, 15}))                    // 14
	println(maxScore([]int{697035, 181412, 384958, 575458})) // 869
}
