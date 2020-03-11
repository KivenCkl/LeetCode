
# @Title: 猜数字 (Guess Numbers)
# @Author: KivenC
# @Date: 2019-10-04 13:38:56
# @Runtime: 64 ms
# @Memory: 13.7 MB

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(1 for a, b in zip(guess, answer) if a == b)
