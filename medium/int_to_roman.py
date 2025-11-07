class Solution:
    def intToRoman(self, num: int) -> str:
        r = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        s = ''
        for i in range(4):
            a = num//10**(3-i)
            if a==0:
                continue
            else:
                num = num%10**(3-i)
                if a<4:
                    s+=f'{r[10**(3-i)]*a}'
                elif a==4:
                    s+=f'{r[10**(3-i)]}{r[10**(3-i)*5]}'
                elif a>8:
                    s+=f'{r[10**(3-i)]}{r[10**(4-i)]}'
                else:
                    s+=f'{r[10**(3-i)*5]}{r[10**(3-i)]*(a-5)}'
        return s