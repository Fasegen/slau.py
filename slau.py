A = []
n = int(input())
for i in range(n):
    A.append((str(input())))
B = []
for i in A:
    if len(i) <= 3:
        B.append(i)
print(B)
