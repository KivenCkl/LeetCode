
# @Title: 简化路径 (Simplify Path)
# @Author: KivenC
# @Date: 2019-05-08 10:49:42
# @Runtime: 56 ms
# @Memory: 13 MB

class Solution:
    def simplifyPath(self, path: str) -> str:
        splited_path = path.split('/')
        res = []
        for p in splited_path:
            if p == '' or p == '.':
                continue
            elif p == '..': 
                if res:
                    res.pop()
            else:
                res.append(p)
        return '/' + '/'.join(res)
                
