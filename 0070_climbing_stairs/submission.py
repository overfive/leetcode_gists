from math import floor
from functools import reduce
from operator import mul

class Solution:
    def climbStairs(self, n: int) -> int:
        ret_sum = 0
        for i in range(0, floor(n/2)+1):
            if i == 0:
                ret_sum += 1
                continue
            ret_sum += int(reduce(mul, range(n-i,n-i-i, -1), 1) / reduce(mul, range(1, i+1), 1))
        return ret_sum
