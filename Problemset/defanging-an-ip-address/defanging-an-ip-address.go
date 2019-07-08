
// @Title: IP 地址无效化 (Defanging an IP Address)
// @Author: KivenC
// @Date: 2019-07-08 13:47:38
// @Runtime: 0 ms
// @Memory: 1.9 MB

func defangIPaddr(address string) string {
    new_addr := []rune{}
    for _, v := range address {
        if v == '.' {
            new_addr = append(new_addr, '[', '.', ']')
        } else {
            new_addr = append(new_addr, v)
        }
    }
    return string(new_addr)
}
