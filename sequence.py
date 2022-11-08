# f = lambda n: 1 if n == 0 else f(n - 1) * n**2

# print([f(n) for n in range(10)])

# f = lambda n: 0 if n ==0 else 1 if n == 1 else f(n - 1) + f(n-2)

# print([f(n) for n in range(5)])


f = lambda n: n ** 2 in range(1, n+1)

result = sum(map(f, range(1,50)))

print(result)