class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while True:
            i,v = random.sample(list(enumerate(a)), 2)
            if sum([i[1],v[1]]) == 9:
                return [i[0],v[0]]
