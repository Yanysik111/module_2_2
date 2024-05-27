first = int(input('Введи первое число: '))
second = int(input('Введи второе число: '))
third = int(input('Введи третье число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second ==third:
    print(2)
else:
    print(0)