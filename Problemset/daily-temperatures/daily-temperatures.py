
# @Title: 每日温度 (Daily Temperatures)
# @Author: KivenC
# @Date: 2019-05-23 13:37:38
# @Runtime: 360 ms
# @Memory: 16.4 MB

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 构建递减栈，后入栈的元素总比栈顶元素小
        stack, res = [], [0] * len(T)
        for i, t in enumerate(T):
            # 比对当前元素与栈顶元素的大小，如果当前元素 > 栈顶元素，弹出栈顶元素，记录两者下标差值
            while stack and T[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
