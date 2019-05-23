
# @Title: 字符串相乘 (Multiply Strings)
# @Author: KivenC
# @Date: 2019-02-27 15:03:23
# @Runtime: 368 ms
# @Memory: 13.1 MB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
        例: 123 * 45,  123的第1位 2 和45的第0位 4 乘积 08 存放在结果的第[1, 2]位中
          index:    0 1 2 3 4  
              
                        1 2 3
                    *     4 5
                    ---------
                          1 5
                        1 0
                      0 5
                    ---------
                      0 6 1 5
                        1 2
                      0 8
                    0 4
                    ---------
                    0 5 5 3 5
        这样我们就可以单独都对每一位进行相乘计算把结果存入相应的index中
        '''
        if num1 == '0' or num2 == '0':
            return '0'
        mul = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                tempMul = int(num1[i]) * int(num2[j])
                tempMul += mul[i+j+1]   # 关键，先加低位判断是否有新的进位
                mul[i+j] += tempMul // 10
                mul[i+j+1] = tempMul % 10
        mul = mul if mul[0] else mul[1:]
        return ''.join(map(str, mul))
