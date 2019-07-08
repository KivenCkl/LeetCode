
// @Title: 大样本统计 (Statistics from a Large Sample)
// @Author: KivenC
// @Date: 2019-06-25 11:09:53
// @Runtime: 4 ms
// @Memory: 2.7 MB

func sampleStats(count []int) []float64 {
	var min, max, mid, common int
	min = 256
	var total, cnt int
	for i := 0; i < 256; i++ {
		if count[i] == 0 {
			continue
		}
		// 样本数
		cnt += count[i]
		// 样本总和
		total += count[i] * i
		// 最小值
		if i < min {
			min = i
		}
		// 最大值
		if i > max {
			max = i
		}
		// 众数
		if count[i] > count[common] {
			common = i
		}
	}
	var mid1, mid2 int
	if cnt%2 == 0 {
		mid1, mid2 = cnt/2, cnt/2+1
	} else {
		mid1, mid2 = cnt/2+1, cnt/2+1
	}
	// 中位数
	for i := 0; i < 256; i++ {
		mid1 -= count[i]
		mid2 -= count[i]
		if mid1 <= 0 {
			mid += i
			mid1 = 2 << 31
		}
		if mid2 <= 0 {
			mid += i
			break
		}
	}
	return []float64{float64(min), float64(max), float64(total) / float64(cnt), float64(mid) / 2, float64(common)}
}

