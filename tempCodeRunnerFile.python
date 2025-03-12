class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        rom = ""
        pos = len(num) - 1
        numbers = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        for i in range(len(num)):
            if num[i] != '4' and num[i] != '9':
                if num[i] < '4':
                    rom += numbers[10**pos] * int(num[i])
                else:
                    rom += (numbers[5* 10**pos] + numbers[10**pos] * (int(num[i])%5))
            else:
                rom += numbers[10**pos] + numbers[(int(num[i])+1) * 10**pos]
            pos -= 1
        return rom





s = Solution()
print(s.intToRoman(58))
print(s.intToRoman(3749))
print(s.intToRoman(1994))