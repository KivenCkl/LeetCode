
// @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
// @Author: KivenC
// @Date: 2019-06-05 17:33:37
// @Runtime: 8 ms
// @Memory: 3.3 MB

func lengthOfLongestSubstring(s string) int {
    // 滑动窗口
    // 如果 s[j] 在 [i, j) 范围内有与 s[j'] 重复的字符，我们不需要逐渐增加 i
    // 我们可以直接跳过 [i，j'] 范围内的所有元素，并将 i 变为 j' + 1
	hashMap := make(map[rune]int)
	i, res := 0, 0
	for j, c := range s {
		i = Max(hashMap[c], i)
		res = Max(res, j-i+1)
		hashMap[c] = j + 1
	}
	return res
}

func Max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

