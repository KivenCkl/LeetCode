
// @Title: 拼车 (Car Pooling)
// @Author: KivenC
// @Date: 2019-07-01 18:05:40
// @Runtime: 8 ms
// @Memory: 3.3 MB

func carPooling(trips [][]int, capacity int) bool {
    // 维护一个列表，index 为站台，value 为乘客数，上客点加，下客点减
    record := [1001]int{}
    for i := 0; i < len(trips); i++ {
        t := trips[i]
        record[t[1]] += t[0]
        record[t[2]] -= t[0]
    }
    // 遍历列表，判断每个站台上车上的乘客数是否超过限制
    for i := 1; i <= 1000; i++ {
        record[i] += record[i-1]
        if record[i] > capacity {
            return false
        }
    }
    return true
}

