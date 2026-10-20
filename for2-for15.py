# For2. Даны два целых числа А и В (A<B). Вывести в порядке возрастания все целые числа, расположенные между А и В (включая сами числа А и В), а также количество N этих чисел.
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print(count)


# For4. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.
price = float(input())
for kg in range(1, 11):
    print(kg * price)


# For5. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.
price = float(input())
for i in range(1, 11):
    kg = i / 10
    print(kg * price)


# For6. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.
price = float(input())
for i in range(12, 21, 2):
    kg = i / 10
    print(kg * price)


# For8. Даны два целых числа А и В (A<B). Найти произведение всех целых чисел от А до В включительно.
a = int(input())
b = int(input())
product = 1
for i in range(a, b + 1):
    product *= i
print(product)


# For9. Даны два целых числа А и В (A<B). Найти сумму квадратов всех целых чисел от А до В включительно.
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    total += i ** 2
print(total)


# For11. Дано целое число N (>0). Найти сумму N^2 + (N+1)^2 + (N+2)^2 + ... + (2*N)^2.
n = int(input())
total = 0
for i in range(n, 2 * n + 1):
    total += i ** 2
print(total)


# For12. Дано целое число N (>0). Найти произведение 1.1 * 1.2 * 1.3 * ... (N сомножителей).
n = int(input())
product = 1.0
for i in range(1, n + 1):
    product *= 1 + i / 10
print(product)


# For13. Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки чередуются).
n = int(input())
total = 0.0
sign = 1
for i in range(1, n + 1):
    total += sign * (1 + i / 10)
    sign = -sign
print(total)


# For15. Дано вещественное число А и целое число N (>0). Найти А в степени N: A^N = A * A * ... * A (число А перемножается N раз).
a = float(input())
n = int(input())
result = 1.0
for _ in range(n):
    result *= a
print(result)