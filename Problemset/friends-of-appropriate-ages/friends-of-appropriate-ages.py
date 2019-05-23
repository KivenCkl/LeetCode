
# @Title: 适龄的朋友 (Friends Of Appropriate Ages)
# @Author: KivenC
# @Date: 2018-07-20 20:33:56
# @Runtime: 724 ms
# @Memory: N/A

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # 年龄取值的范围比较小，1 <= ages[i] <= 120, 所以可以把所有的年龄都转换成(age, count)这样一个对，用dic记录，然后dic[age]代表年龄为age的人有多少个。反正匹配只和年龄有关，这个人的序号无关，所以对于年龄进行O(n2)=O(120**2)的遍历
        dic = {}
        for age in ages:
            if age in dic:
                dic[age] += 1
            else:
                dic[age] = 1
        res = 0
        for age in ages:
            # 计算当前年龄下符合计算公式的人数，要排除自己，因此减一
            dic[age] -= 1
            # 符合条件的区间
            left, right = age // 2 + 8, age
            res += sum(dic[x] for x in range(left, right+1) if x in dic)
            # 把自己加回来
            dic[age] += 1
        return res
