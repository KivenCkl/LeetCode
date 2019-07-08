
// @Title: 解析布尔表达式 (Parsing A Boolean Expression)
// @Author: KivenC
// @Date: 2019-07-08 11:39:07
// @Runtime: 0 ms
// @Memory: 2.6 MB

// // way 1
// func parseBoolExpr(expression string) bool {
//     switch expression{
//         case "":return true
//         case "t":return true
//         case "f":return false
//     }
//     if expression[0]=='!'{
//         return !parseBoolExpr(expression[2:len(expression)-1])
//     }
//     if expression[0]=='&'{
//         exps:=split(expression[2:len(expression)-1])
//         for i:=range exps{
//             if !parseBoolExpr(exps[i]){
//                 return false
//             }
//         }
//         return true
//     }
//     if expression[0]=='|'{
//         exps:=split(expression[2:len(expression)-1])
//         for i:=range exps{
//             if parseBoolExpr(exps[i]){
//                 return true
//             }
//         }
//         return false
//     }
//     return true
// }

// func split(s string)[]string{
//     stack:=make([]byte,0)
//     result:=make([]string,0)
//     for i:=0;i<len(s);i++{
//         if s[i]=='('||s[i]=='{'{
//             stack=append(stack,s[i])
//         }
//         if s[i]==')'||s[i]=='}'{
//             stack=stack[:len(stack)-1]
//         }
//         if len(stack)==0&&s[i]==','{
//             result=append(result,s[:i])           
//             s=s[i+1:]
//             i=0
//         }
//     }
//     result=append(result,s)
//     return result
// }

// way 2
// 双栈
func parseBoolExpr(expression string) bool {
	v, op := []rune{}, []rune{} // 双栈，分别记录表达式和操作符
    tf := []rune{'f', 't'}
	for _, c := range expression {
		switch c {
		case ',':
			break
		case '|', '&', '!':
			op = append(op, c)
		case ')':
			t, f := 0, 0 // 用于标记是否存在 t/f
            for v[len(v)-1] != '(' {
				if v[len(v)-1] == 'f' {
					f = 1
				} else {
					t = 1
				}
                v = v[:len(v)-1]
			}
			v = v[:len(v)-1] // 将左括号 ( 出栈

            switch op[len(op)-1] {
			case '|':
                // 存在 t 即为真
				v = append(v, tf[t])
			case '&':
                // 存在 f 即为假
				v = append(v, tf[1-f])
			case '!':
                // 存在 f 为真
				v = append(v, tf[f])
			}
			op = op[:len(op)-1]
		default:
			v = append(v, c)
		}
	}
	return v[0] == 't'
}

