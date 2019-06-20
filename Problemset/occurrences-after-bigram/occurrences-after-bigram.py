
# @Title: Bigram 分词 (Occurrences After Bigram)
# @Author: KivenC
# @Date: 2019-06-15 10:24:18
# @Runtime: 48 ms
# @Memory: 13 MB

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        splited_text = text.split(' ')
        interval = 2 if first != second else 1
        i, res = 0, []
        while i < len(splited_text) - 2:
            if splited_text[i] == first and splited_text[i+1] == second:
                res.append(splited_text[i+2])
                i += interval
            else:
                i += 1
        return res
            
