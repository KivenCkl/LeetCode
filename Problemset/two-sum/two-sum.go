
// @Title: 两数之和 (Two Sum)
// @Author: KivenC
// @Date: 2019-06-04 16:34:19
// @Runtime: 0 ms
// @Memory: 3.8 MB

func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int)
    for i, v := range nums {
        if j, ok := hashmap[target-v]; ok {
            return []int{j, i}
        }
        hashmap[v] = i
    }
    return nil
}
