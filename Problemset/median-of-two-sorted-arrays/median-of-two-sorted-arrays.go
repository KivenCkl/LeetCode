
// @Title: 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)
// @Author: KivenC
// @Date: 2019-06-05 17:32:53
// @Runtime: 24 ms
// @Memory: 5.6 MB

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// 假设 len(A) < len(B)
	// 将 A 列表在位置 i 上划分为 left_A[:i] 和 right_A[i:]
	// 将 B 列表在位置 j 上划分为 left_B[:j] 和 right_B[j:]
	// i+j = len(A)-i+len(B)-j 且 left_A[i-1] < right_B[j] 且 left_B[j-1] < right_A[i]
	// 则 res = (max(left_part) + max(right_part)) / 2
	m, n := len(nums1), len(nums2)

	if m > n {
		nums1, nums2, m, n = nums2, nums1, n, m
	}
	var i, j int

	for lo, hi, half_len := 0, m, (m+n+1)/2; lo <= hi; {
		i = (lo + hi) / 2
		j = half_len - i

		if i < m && nums1[i] < nums2[j-1] {
			lo = i + 1
		} else if i > 0 && nums1[i-1] > nums2[j] {
			hi = i - 1
		} else {
			break
		}
	}
	var left, right int

	if i == 0 {
		left = nums2[j-1]
	} else if j == 0 {
		left = nums1[i-1]
	} else {
		left = Max(nums1[i-1], nums2[j-1])
	}

	if (m+n)%2 == 1 {
        return float64(left)
	}

	if i == m {
		right = nums2[j]
	} else if j == n {
		right = nums1[i]
	} else {
		right = Min(nums1[i], nums2[j])
	}

	return float64(left + right) / 2
}

func Min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func Max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

