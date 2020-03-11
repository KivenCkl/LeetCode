
// @Title: x 的平方根 (Sqrt(x))
// @Author: KivenC
// @Date: 2019-07-16 10:02:41
// @Runtime: 4 ms
// @Memory: 2.2 MB

func mySqrt(x int) int {
	// 牛顿法
	// 迭代公式：x_i = 1/2*(x_(i-1)+a/x_(i-1))
    cur := x
    for cur*cur > x {
        cur = (cur + x/cur) / 2
    }
    return cur
}

