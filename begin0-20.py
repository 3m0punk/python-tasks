# Begin1. Дана сторона квадрата a. Найти его периметр P = 4 * a
a = float(input())
perimeter = 4 * a
print(perimeter)

# Begin2. Дана сторона квадрата a. Найти его площадь S = a^2
side = float(input())
area = side ** 2
print(area)

# Begin3. Даны стороны прямоугольника a и b. Найти его площадь S = a * b и периметр P = 2 * (a + b)
a = float(input())
b = float(input())
area = a * b
perimeter = 2 * (a + b)
print(area)
print(perimeter)

# Begin4. Дан диаметр окружности d. Найти ее длину L = pi * d. В качестве значения pi использовать 3.14
d = float(input())
pi = 3.14
length = pi * d
print(length)

# Begin5. Дана длина ребра куба a. Найти объем куба V = a^3 и площадь его поверхности S = 6 * a^2
a = float(input())
volume = a ** 3
surface = 6 * a ** 2
print(volume)
print(surface)

# Begin6. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a * b * c и площадь поверхности S = 2 * (a * b + b * c + a * c)
a = float(input())
b = float(input())
c = float(input())
volume = a * b * c
surface = 2 * (a * b + b * c + a * c)
print(volume)
print(surface)

# Begin7. Найти длину окружности L и площадь круга S заданного радиуса R: L = 2 * pi * R, S = pi * R^2. В качестве значения pi использовать 3.14
r = float(input())
pi = 3.14
length = 2 * pi * r
area = pi * r ** 2
print(length)
print(area)

# Begin8. Даны два числа a и b. Найти их среднее арифметическое: (a + b) / 2
a = float(input())
b = float(input())
average = (a + b) / 2
print(average)

# Begin9. СЛОЖНОЕ. Даны два неотрицательных числа a и b. Найти их среднее геометрическое: sqrt(a * b)
a = float(input())
b = float(input())
geom_average = (a * b) ** 0.5
print(geom_average)

# Begin10. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов
a = float(input())
b = float(input())
a2 = a ** 2
b2 = b ** 2
print(a2 + b2)
print(a2 - b2)
print(a2 * b2)
print(a2 / b2)

# Begin11. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей
a = float(input())
b = float(input())
abs_a = abs(a)
abs_b = abs(b)
print(abs_a + abs_b)
print(abs_a - abs_b)
print(abs_a * abs_b)
print(abs_a / abs_b)

# Begin12. СЛОЖНОЕ. Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу c и периметр P: c = sqrt(a^2 + b^2), P = a + b + c
a = float(input())
b = float(input())
c = (a ** 2 + b ** 2) ** 0.5
perimeter = a + b + c
print(c)
print(perimeter)

# Begin13. СЛОЖНОЕ. Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2). Найти площади S1, S2 и S3 кольца: S1 = pi * R1^2, S2 = pi * R2^2, S3 = S1 - S2. В качестве pi использовать 3.14
r1 = float(input())
r2 = float(input())
pi = 3.14
s1 = pi * r1 ** 2
s2 = pi * r2 ** 2
s3 = s1 - s2
print(s1)
print(s2)
print(s3)

# Begin14. СЛОЖНОЕ. Дана длина L окружности. Найти ее радиус R и площадь S круга: L = 2 * pi * R, S = pi * R^2. В качестве pi использовать 3.14
length = float(input())
pi = 3.14
r = length / (2 * pi)
area = pi * r ** 2
print(r)
print(area)

# Begin15. СЛОЖНОЕ. Дана площадь S круга. Найти его диаметр D и длину L окружности: L = 2 * pi * R, S = pi * R^2. В качестве pi использовать 3.14
area = float(input())
pi = 3.14
r = (area / pi) ** 0.5
d = 2 * r
length = 2 * pi * r
print(d)
print(length)

# Begin16. Найти расстояние между двумя точками с заданными координатами x1 и x2 на числовой оси: |x2 - x1|
x1 = float(input())
x2 = float(input())
distance = abs(x2 - x1)
print(distance)

# Begin17. Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму
a = float(input())
b = float(input())
c = float(input())
ac = abs(c - a)
bc = abs(c - b)
sum_ac_bc = ac + bc
print(ac)
print(bc)
print(sum_ac_bc)

# Begin18. СЛОЖНОЕ. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC
a = float(input())
b = float(input())
c = float(input())
ac = abs(c - a)
bc = abs(c - b)
prod_ac_bc = ac * bc
print(prod_ac_bc)

# Begin19. СЛОЖНОЕ. Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2). Стороны параллельны осям. Найти периметр и площадь
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
width = abs(x2 - x1)
height = abs(y2 - y1)
perimeter = 2 * (width + height)
area = width * height
print(perimeter)
print(area)

# Begin20. СЛОЖНОЕ. Найти расстояние между двумя точками (x1, y1) и (x2, y2) на плоскости: sqrt((x2 - x1)^2 + (y2 - y1)^2)
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)
