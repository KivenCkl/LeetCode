
# @Title: 不同字符的最小子序列 (Smallest Subsequence of Distinct Characters)
# @Author: KivenC
# @Date: 2019-06-19 15:44:23
# @Runtime: 52 ms
# @Memory: 13 MB

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        # 维护一个栈，遍历 text 如果该字符小于栈顶元素且在该字符后面仍存在栈顶元素，则弹出
        # 优化，先统计 text 中每个字符出现的次数，第二次遍历时每出现一次减一，当 >0 则表示后面仍存在
        import collections
        counter = collections.Counter(text)  # 统计字符出现次数
        stack = []
        visited = collections.defaultdict(int)  # 记录字符是否存在于栈中
        for c in text:
            counter[c] -= 1
            if visited[c]:
                continue
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                tmp = stack.pop()
                visited[tmp] = 0
            stack.append(c)
            visited[c] = 1
        return "".join(stack)
