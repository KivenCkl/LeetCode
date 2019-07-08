
// @Title: 分糖果 II (Distribute Candies to People)
// @Author: KivenC
// @Date: 2019-07-03 18:45:30
// @Runtime: 0 ms
// @Memory: 6.3 MB

func distributeCandies(candies int, num_people int) []int {
	// 模拟分发的过程
	res := make([]int, num_people)
    for step := 0; candies > 0; step++ {
		res[step%num_people] += min(candies, step+1)
		candies -= step + 1
	}
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

