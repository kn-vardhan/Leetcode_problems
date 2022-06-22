class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        val1 = num1.split('+')
        val2 = num2.split('+')        
        val1[1] = val1[1].split('i')
        val2[1] = val2[1].split('i')

        real = int(val1[0])*int(val2[0]) - int(val1[1][0])*int(val2[1][0])
        img = int(val1[0])*int(val2[1][0]) + int(val2[0])*int(val1[1][0])
        real = str(real)
        img = "+" + str(img) + "i"
        
        return real+img


