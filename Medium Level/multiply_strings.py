class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        i_s = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        
        number1 = 0
        number2 = 0
        n1 = len(num1)
        n2 = len(num2)
        for i in range(n1):
            number1 += (ord(num1[i]) - (ord('0'))) * pow(10, (n1-i-1))
        for i in range(n2):
            number2 += (ord(num2[i]) - (ord('0'))) * pow(10, (n2-i-1))
        new_number = number1 * number2

        if new_number == 0:
            return "0"

        answer = ''
        pointer = 10
        while new_number > 0:
            value = new_number % pointer
            answer += i_s[value]
            new_number = new_number // pointer

        return answer[::-1]


