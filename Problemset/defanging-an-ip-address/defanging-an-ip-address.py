
# @Title: IP 地址无效化 (Defanging an IP Address)
# @Author: KivenC
# @Date: 2019-07-08 11:42:09
# @Runtime: 52 ms
# @Memory: 12.9 MB

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
