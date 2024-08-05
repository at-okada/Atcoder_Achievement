R = int(input())

ones = R % 10
print(ones)

tens = (R // 10) % 10
print(tens)

two_digit_number = tens * 10 + ones

result = 100 - two_digit_number

print(result)