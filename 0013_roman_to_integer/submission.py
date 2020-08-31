class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        rs = s[::-1]
        for p,v in enumerate(rs):
            if p == 0:
                ret = ret + map[v]
            else:
                if map[v] >= map[rs[p-1]]:
                    ret = ret + map[v]
                else:
                    ret = ret - map[v]

        return ret
