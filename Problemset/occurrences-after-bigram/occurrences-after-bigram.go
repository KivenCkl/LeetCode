
// @Title: Bigram 分词 (Occurrences After Bigram)
// @Author: KivenC
// @Date: 2019-06-15 10:32:23
// @Runtime: 0 ms
// @Memory: 2.1 MB

func findOcurrences(text string, first string, second string) []string {
    splited_text := strings.Fields(text)
    res := []string{}
    interval := 2
    
    if first == second {
        interval = 1
    }
    
    for i := 0; i < len(splited_text)-2; {
        if splited_text[i] == first && splited_text[i+1] == second {
            res = append(res, splited_text[i+2])
            i += interval
        } else {
            i += 1
        }
    }
    return res
}
