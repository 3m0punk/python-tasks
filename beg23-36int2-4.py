# Begin23
a = float(input())
b = float(input())
c = float(input())
temp = a
a = b
b = c
c = temp
print(a)
print(b)
print(c)

# Begin24
a = float(input())
b = float(input())
c = float(input())
temp = a
a = c
c = b
b = temp
print(a)
print(b)
print(c)

# Begin26
x = float(input())
y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
print(y)

# Begin27
a = float(input())
a2 = a * a
a4 = a2 * a2
a8 = a4 * a4
print(a2)
print(a4)
print(a8)

# Begin28
a = float(input())
a2 = a * a
a3 = a2 * a
a5 = a3 * a2
a10 = a5 * a5
a15 = a10 * a5
print(a2)
print(a3)
print(a5)
print(a10)
print(a15)

# Begin30
radians = float(input())
pi = 3.14
degrees = radians * 180 / pi
print(degrees)

# Begin31
tf = float(input())
tc = (tf - 32) * 5 / 9
print(tc)

# Begin32
tc = float(input())
tf = tc * 9 / 5 + 32
print(tf)

# Begin33
x = float(input())
a = float(input())
y = float(input())
price_per_kg = a / x
total_price = price_per_kg * y
print(price_per_kg)
print(total_price)

# Begin34
x = float(input())
a = float(input())
y = float(input())
b = float(input())
price_choc = a / x
price_iris = b / y
ratio = price_choc / price_iris
print(price_choc)
print(price_iris)
print(ratio)

# Begin35
v = float(input())
u = float(input())
t1 = float(input())
t2 = float(input())
s = v * t1 + (v - u) * t2
print(s)

# Begin36
v1 = float(input())
v2 = float(input())
s = float(input())
t = float(input())
s_total = s + (v1 + v2) * t
print(s_total)

# Integer2
mass_kg = int(input())
tons = mass_kg // 1000
print(tons)

# Integer3
file_bytes = int(input())
kilobytes = file_bytes // 1024
print(kilobytes)

# Integer4
segment_a = int(input())
segment_b = int(input())
count = segment_a // segment_b
print(count)