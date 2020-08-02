
# @Title: 子域名访问计数 (Subdomain Visit Count)
# @Author: KivenC
# @Date: 2020-07-31 14:33:18
# @Runtime: 60 ms
# @Memory: 13.7 MB

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        record = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)
            domain_list = domain.split('.')
            for i in range(len(domain_list)):
                key = ".".join(domain_list[i:])
                record[key] = record.get(key, 0) + count
        return [f"{v} {k}" for k, v in record.items()]

