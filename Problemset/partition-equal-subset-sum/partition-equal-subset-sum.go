
// @Title: 分割等和子集 (Partition Equal Subset Sum)
// @Author: KivenC
// @Date: 2019-07-13 11:07:43
// @Runtime: 8 ms
// @Memory: 2.7 MB

// // way 1
// // 动态规划
// func canPartition(nums []int) bool {
//     total := 0
//     for _, num := range nums {
//         total += num
//     }
//     if total%2 == 1 {
//         return false
//     }
//     target := total / 2
//     dp := make([]bool, target+1)
//     dp[0] = true
    
//     for i := 0; i < len(nums); i++ {
//         for j := target; j >= nums[i]; j-- {
//             dp[j] = dp[j] || dp[j-nums[i]]
//         }
//         if dp[target] {
//             return true
//         }
//     }
//     return false
// }

// way 2
// 回溯
func canPartition(nums []int) bool {
    total := 0
    dp := map[int]int{}
    for _, num := range nums {
        total += num
        dp[num]++
    }
    if total%2 == 1 {
        return false
    }
    return helper(dp, total/2)
}

func helper(dp map[int]int, target int) bool {
    if target == 0 {
        return true
    }
    if len(dp) == 0 {
        return false
    }
    for k, _ := range dp {
        dp[k]--
        if dp[k] == 0 {
            delete(dp, k)
        }
        if target-k >= 0 && helper(dp, target-k) {
            return true
        }
        dp[k]++
    }
    return false
}

