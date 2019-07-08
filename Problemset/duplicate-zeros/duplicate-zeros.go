
// @Title: 复写零 (Duplicate Zeros)
// @Author: KivenC
// @Date: 2019-07-01 22:10:27
// @Runtime: 76 ms
// @Memory: 8.3 MB

func duplicateZeros(arr []int) {
	//  // way 1
	// 	// 借用数组副本辅助
	// 	cop := make([]int, len(arr))
	// 	copy(cop, arr)

	// 	for i, j := 0, 0; j < len(arr); {
	// 		arr[j] = cop[i]
	// 		if cop[i] == 0 {
	// 			if j++; j < len(arr) {
	// 				arr[j] = 0
	// 			}
	// 		}
	// 		j++
	// 		i++
	// 	}

	// way 2
	// 双指针
	n := len(arr)
	i, j := 0, 0
	// 第一次遍历
	for i = 0; i < n; i, j = i+1, j+1 {
		if arr[i] == 0 {
			j++
		}
	}
	// 第二次反向遍历
	for i = n - 1; i >= 0; i-- {
		j--
		if j < n {
			arr[j] = arr[i]
		}
		if arr[i] == 0 {
			j--
			if j < n {
				arr[j] = 0
			}
		}
	}
}

