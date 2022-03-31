#to check the given number is armstrong or not

number = int(input())
sum = 0
temp = number

while temp > 0:

    digit = temp % 10
    sum += digit ** 3
    temp //= 10


if number == sum:
    print(True)
else:
    print(False)
