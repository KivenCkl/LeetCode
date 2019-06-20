
// @Title: 按列翻转得到最大值等行数 (Flip Columns For Maximum Number of Equal Rows)
// @Author: KivenC
// @Date: 2019-06-14 14:18:25
// @Runtime: 312 ms
// @Memory: 6.6 MB

func maxEqualRowsAfterFlips(matrix [][]int) int {
	// 用一个元组记录每一行的特征
	// 如果第一个元素为 1 则翻转该行
	// 例如 "[1, 0, 1, 1, 1, 0, 0, 1]" 记为 "01000110"
	// 具有相同特征的行代表可以通过翻转得到相同结果
	mapper := make(map[string]int)
	res := 0
	for _, row := range matrix {
        tmp := make([]byte, len(row))
        
        for i, v := range row {
            if v == row[0] {
                tmp[i] = '1'
            } else {
                tmp[i] = '0'
            }
        }

        key := string(tmp)
        mapper[key]++

		if mapper[key] > res {
			res = mapper[key]
		}
	}
	return res
}

