
# @Title: 字符串转换整数 (atoi) (String to Integer (atoi))
# @Author: KivenC
# @Date: 2019-01-02 10:45:59
# @Runtime: 84 ms
# @Memory: 6.6 MB

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        allowed_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        allowed_list_ext = allowed_list + ['+', '-']
        ans_str = ''
        str = str.lstrip()
        try:
            if str[0] in allowed_list_ext:
                ans_str += str[0]
                for s in str[1:]:
                    if  s in allowed_list:
                        ans_str += s
                    else:
                        break
                ans_int = int(ans_str)
                if ans_int <= INT_MIN:
                    return INT_MIN
                elif ans_int >= INT_MAX:
                    return INT_MAX
                else:
                    return ans_int
            return 0
        except:
            return 0
        
