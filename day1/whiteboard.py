# Given two non-negative integers num1 and num2 represented as string, 
# return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# Example:
# Input: num1 = "30", num2 = "10"
# Output: 40
# The output should be given as an integer

def number(str1, str2):
    # if len(str1) + len(str2) < 5100:
        return int(str1) + int(str2)

num1 = "30"
num2 = "10"
print(number(num1, num2))

