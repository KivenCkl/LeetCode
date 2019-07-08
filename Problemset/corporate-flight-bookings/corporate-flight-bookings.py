
# @Title: 航班预订统计 (Corporate Flight Bookings)
# @Author: KivenC
# @Date: 2019-07-08 14:27:37
# @Runtime: 336 ms
# @Memory: 23 MB

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for booking in bookings:
            ans[booking[0]-1] += booking[2]
            ans[booking[1]] -= booking[2]
        for i in range(1, n+1):
            ans[i] += ans[i-1]
        return ans[:n]
