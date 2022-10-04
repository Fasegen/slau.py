A = []
print("Введите длину массива")
n = int(input())
print("Введите строки")
for i in range(n):
    A.append((str(input())))
B = []
for i in A:
    if len(i) <= 3:         #Условие задачи, что длина меньше или равна 3 символам
        B.append(i)
print(B)
