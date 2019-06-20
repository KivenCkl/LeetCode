
// @Title: 字符串的最大公因子 (Greatest Common Divisor of Strings)
// @Author: KivenC
// @Date: 2019-06-13 21:06:18
// @Runtime: 0 ms
// @Memory: 2.6 MB

func gcdOfStrings(str1 string, str2 string) string {
	// str1 + str2 != str2 + str1 是存在公因子的充要条件
	// 两个字符串的最大公因子的长度，必定是两个字符串长度的最大公约数，否则无法被除尽
	if str1+str2 != str2+str1 {
		return ""
	}
	return str1[:Gcd(len(str1), len(str2))]
}

func Gcd(a, b int) int {
	// if b == 0 {
	// 	return a
	// } else {
	// 	return Gcd(b, a%b)
	// }
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

