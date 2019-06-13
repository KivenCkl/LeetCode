
// @Title: 最长回文子串 (Longest Palindromic Substring)
// @Author: KivenC
// @Date: 2019-06-13 16:18:06
// @Runtime: 4 ms
// @Memory: 3.3 MB

// // way 1
// // 从回文串的中心向两边扩展，O(n^2)
// // 分奇数串和偶数串
// func longestPalindrome(s string) string {
// 	if len(s) < 2 {
// 		return s
// 	}
// 	start, end := 0, 0
// 	for i, _ := range s {
// 		len_odd := expandAroundCenter(s, i, i)    // 奇数串
// 		len_even := expandAroundCenter(s, i, i+1) // 偶数串
// 		res := Max(len_odd, len_even)
// 		if res > end-start {
// 			start = i - (res-1)/2
// 			end = i + res/2
// 		}
// 	}
// 	return s[start : end+1]
// }

// func expandAroundCenter(s string, l, r int) int {
// 	for l >= 0 && r < len(s) && s[l] == s[r] {
// 		l--
// 		r++
// 	}
// 	return r - l - 1
// }

// func Max(a, b int) int {
// 	if a > b {
// 		return a
// 	} else {
// 		return b
// 	}
// }

// way 2
// Manacher 算法
// O(n)
func longestPalindrome(s string) string {
	var b bytes.Buffer
	b.WriteString("&#")
	for _, c := range s {
		b.WriteString(string(c) + "#")
	}
	new_s := b.String()
	mx, ct, resLen, resCenter := 0, 0, 0, 0
	p := make([]int, len(new_s))
	for i := 1; i < len(new_s); i++ {
		if mx > i {
			p[i] = Min(p[2*ct-i], mx-i)
		} else {
			p[i] = 1
		}
		for i-p[i] >= 0 && i+p[i] < len(new_s) && new_s[i+p[i]] == new_s[i-p[i]] {
			p[i]++
		}
		if mx < i+p[i]-1 {
			mx = i + p[i] - 1
			ct = i
		}
		if resLen < p[i] {
			resLen = p[i]
			resCenter = i
		}
	}
	return s[(resCenter-resLen+1)/2 : (resCenter+resLen-1)/2]
}

func Min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

