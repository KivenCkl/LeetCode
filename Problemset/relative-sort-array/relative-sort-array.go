
// @Title: 数组的相对排序 (Relative Sort Array)
// @Author: KivenC
// @Date: 2019-07-18 15:10:00
// @Runtime: 8 ms
// @Memory: 6.1 MB

func relativeSortArray(arr1 []int, arr2 []int) []int {
    // 统计 arr1 中元素
    counter := map[int]int{}
    for _, k := range arr1 {
        counter[k]++
    }
    res := []int{}
    // 先将 arr2 中存在的元素排好
    for _, k := range arr2 {
        for counter[k] > 0 {
            res = append(res, k)
            counter[k]--
        }
    }
    // 将 arr2 中不存在的元素按升序排好
    for i := 0; i <= 1000; i++ {
        for counter[i] > 0 {
            res = append(res, i)
            counter[i]--
        }
    }
    return res
}
