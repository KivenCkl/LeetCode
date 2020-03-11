
// @Title: 数组中的第K个最大元素 (Kth Largest Element in an Array)
// @Author: KivenC
// @Date: 2019-07-09 14:45:59
// @Runtime: 12 ms
// @Memory: 5.2 MB

func findKthLargest(nums []int, k int) int {
    // 利用快排的思想
    tmp := nums[len(nums)/2]
    var l, m, r []int
    for _, num := range nums {
        switch {
        case num > tmp:
            l = append(l, num)
        case num == tmp:
            m = append(m, num)
        case num < tmp:
            r = append(r, num)
        }
    }
    if k <= len(l) {
        return findKthLargest(l, k)
    } else if k <= len(l)+len(m) {
        return tmp
    } else {
        return findKthLargest(r, k-len(l)-len(m))
    }
}

