
// @Title: 负二进制数相加 (Adding Two Negabinary Numbers)
// @Author: KivenC
// @Date: 2019-06-14 16:44:39
// @Runtime: 8 ms
// @Memory: 7.5 MB

func addNegabinary(arr1 []int, arr2 []int) []int {
	// 对 arr1 和 arr2 从后往前依次相加，逢二进一，构造新列表
	res := []int{}
	i, j, carry := len(arr1)-1, len(arr2)-1, 0
	for i > -1 || j > -1 || carry != 0 {
		if i > -1 {
			carry += arr1[i]
			i--
		}
		if j > -1 {
			carry += arr2[j]
			j--
		}
		mod := carry % -2
		carry = carry / -2
		if mod < 0 {
			mod += 2
			carry++
		}
		res = append(res, mod)
	}

	// 倒转列表
	ans := []int{}
	for i := len(res) - 1; i >= 0; i-- {
		ans = append(ans, res[i])
	}

	// 去除前导零
    for i, v := range ans {
        if v != 0 {
            return ans[i:]
        }
	}
    return []int{0}
}

