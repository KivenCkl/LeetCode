
// @Title: 活字印刷 (Letter Tile Possibilities)
// @Author: KivenC
// @Date: 2019-06-15 12:56:28
// @Runtime: 16 ms
// @Memory: 1.9 MB

func numTilePossibilities(tiles string) int {
    // 回溯算法
    // 参考 https://leetcode-cn.com/problems/letter-tile-possibilities/solution/hui-su-suan-fa-python-dai-ma-by-liweiwei1419
    record := map[rune]int{}
    for _, tile := range tiles {
        record[tile]++
    }
    return dfs(record)
}

func dfs(record map[rune]int) int {
    res := 0
    for k, v := range record {
        if v == 0 {
            continue
        }
        res++
        record[k]--
        res += dfs(record)
        record[k]++
    }
    return res
}

