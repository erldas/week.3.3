# 5)Напишите функцию которая принимает: день, месяц, год
# и возвращает 'True' если такая дата есть, если нет то 'False'



day = int(input())
if day > 0 and day <= 31:
    print('True')
else:
    print('False')


month = int(input())
if month >0 and month <= 12:
    print('True')
else:
    print('False')

year = int(input())
if year > 0 and year <= 9999:
    print('True')
else:
    print('False')

