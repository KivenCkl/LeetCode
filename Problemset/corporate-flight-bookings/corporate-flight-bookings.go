
// @Title: 航班预订统计 (Corporate Flight Bookings)
// @Author: KivenC
// @Date: 2019-07-08 14:25:38
// @Runtime: 2120 ms
// @Memory: 8.9 MB

func corpFlightBookings(bookings [][]int, n int) []int {
    ans := make([]int, n+1)
    for _, booking := range bookings {
        ans[booking[0]-1] += booking[2]
        ans[booking[1]] -= booking[2]
    }
    for i := 1; i < n+1; i++ {
        ans[i] += ans[i-1]
    }
    return ans[:n]
}

