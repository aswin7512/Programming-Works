class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'$': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = ''
        cnt = 1
        num = 0
        for i in range(len(s)):
            if s[i] != 'I' and s[i] != 'X' and s[i] != 'C':
                if l != '':
                    if numbers[s[i]] > numbers[l]:
                        num += numbers[s[i]] - numbers[l]
                    else:
                        num += numbers[s[i]] + numbers[l]
                else:
                    num += numbers[s[i]]
            else:
                l = s[i]
        return num




s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))