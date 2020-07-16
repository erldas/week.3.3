# 6)Напишите функцию которая принимает 3-значное число 
# и выводит сумму его цифр


def s(a):
    result = 0
    while a > 0:
        result += a % 10
        a //= 10
    return result
 
print(s(567))


x=321
print(sum(map(int,str(x))))