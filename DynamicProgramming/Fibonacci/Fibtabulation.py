def fib(n):
    table = [0] * (n+1)
    table[1] = 1
    for i in range(n):
        try:
            table[i+1] += table[i]
            table[i+2] += table[i]
        except IndexError:
            pass
    print(table)
    return table[n]

print(fib(5))

#jika ingin hanya menggunakan 2 array
table = [0] * 2
table[1] = 1
n = 5
for i in range(int(n/2)):
    if i + 1 <= n+1:
        table[0] += table[1]
    if i + 2 <= n+1:
        table[1] += table[0]
print(table)

# atau seperti ini untuk bagian for nya jika tidak ingin pakai try
# for i in range(n + 1):
#     if i + 1 <= n:
#         table[i + 1] += table[i]
#     if i + 2 <= n:
#         table[i + 2] += table[i]