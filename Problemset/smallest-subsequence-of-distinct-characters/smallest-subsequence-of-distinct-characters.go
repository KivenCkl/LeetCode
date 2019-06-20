
// @Title: 不同字符的最小子序列 (Smallest Subsequence of Distinct Characters)
// @Author: KivenC
// @Date: 2019-06-19 17:06:34
// @Runtime: 0 ms
// @Memory: 2 MB

func smallestSubsequence(text string) string {
    // 维护一个栈，遍历 text 如果该字符小于栈顶元素且在该字符后面仍存在栈顶元素，则弹出
	counter := map[rune]int{}  // 统计 text 中字符的个数
	stack := []rune{}  // 栈，记录正确的子序列
	visited := map[rune]bool{}  // 记录字符是否出现在 stack
    
	for _, c := range text {
		counter[c]++
	}
    
	for _, c := range text {
		counter[c]--
		if visited[c] {
			continue
		}
        
		for len(stack) != 0 && stack[len(stack)-1] > c && counter[stack[len(stack)-1]] > 0 {
			visited[stack[len(stack)-1]] = false
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, c)
		visited[c] = true
	}
	return string(stack)
}

