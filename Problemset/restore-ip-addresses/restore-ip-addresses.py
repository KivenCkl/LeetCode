
# @Title: 复原IP地址 (Restore IP Addresses)
# @Author: KivenC
# @Date: 2020-08-10 00:05:02
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        if 4 <= len(s) <= 12:
            self.helper(s, [])
        return self.res
    
    def helper(self, s, ip_list):
        if len(ip_list) == 4:
            if not s:
                self.res.append(".".join(ip_list))
            return
        for i in range(1, min(4, len(s) + 1)):
            tmp = s[:i]
            if 0 <= int(tmp) <= 255 and str(int(tmp)) == tmp:
                self.helper(s[i:], ip_list + [tmp])

