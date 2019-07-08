
# @Title: 解析布尔表达式 (Parsing A Boolean Expression)
# @Author: KivenC
# @Date: 2019-07-08 09:31:46
# @Runtime: 100 ms
# @Memory: 12.9 MB

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        opt_set = {"!", "&", "|"}
        exp_set = {"t", "f"}
        stack = []  # 记录表达式
        
        for c in expression:
            # 跳过其他无用信息
            if c in opt_set | exp_set:
                stack.append(c)
            
            if c == ")":
                tmp = set()  # 临时储存每次操作的 t / f
                
                # 出栈直至遇到操作符
                while stack[-1] in exp_set:
                    tmp.add(stack.pop())
                
                opt = stack.pop()
                
                # 不同操作符不同处理方式
                if opt == "!":
                    t = "t" if "f" in tmp else "f"
                elif opt == "&":  # 只要有 f 即为假
                    t = "f" if "f" in tmp else "t"
                elif opt == "|":  # 只要有 t 即为真
                    t = "t" if "t" in tmp else "f"
                
                stack.append(t)
                
        return stack[-1] == "t"
