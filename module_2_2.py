third = input('введите первое число:')
first = input('введите второе число:')
second = input('введите третье число:')
if first == second and third == second:
    print(3)
elif second == first or second == third:
    print(2)
else:
    print(0)