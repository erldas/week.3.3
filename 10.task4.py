# 4)Напишите функцию которая определяет является ли введенное слово 
# палиндромом (палиндром - слово которая читается пишется 
# одинаково справа налево, и слева направо )

def obratka():
    a = str(input())
    b =''.join(reversed(a))
    # print(b)
    if a == b:
        print('True')
    
    else:
        print('False')

obratka()

