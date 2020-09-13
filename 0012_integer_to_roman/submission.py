class Solution:
    map = {
        1: ["I", "V"],
        10: ["X", "L"],
        100: ["C", "D"],
        1000: ["M"]
    }
    def intToRoman(self, num: int) -> str:
        return self.intToRomanL(num, 1)

    def intToRomanL(self, num: int, l: int) -> str:
        if num < 10:
            if num == 0:
                return ""
            if num == 1:
                return self.map[l][0]
            elif num == 4:
                return self.map[l][0] + self.map[l][1]
            elif num == 5:
                return self.map[l][1]
            elif num == 9:
                return self.map[l][0] + self.map[l*10][0]
            elif num < 4:
                return self.map[l][0] + self.intToRomanL(num - 1, l)
            elif num > 5:
                return self.map[l][1] + self.intToRomanL(num - 5, l)
        else:
            t = num  % 10
            return self.intToRomanL((num - t )/10, l * 10) +  self.intToRomanL(t, l)
