a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
if b > a:
    d = a
    a = b
    b = d
    if c > a:
        d = a
        a = c
        c = d
    else:
        a = a
        c = c
else:
    if c > a:
        d = a
        a = c
        c = d
    else:
        a = a
        c = c

if (a >= b + c) or (b >= a + c) or (c >= a + b):
    print("NAO FORMA TRIANGULO")
else:
    a2 = float(a * a)
    b2 = float(b * b)
    c2 = float(c * c)
    if (a2 == b2 + c2):
        print("TRIANGULO RETANGULO")
    elif (a2 < b2 + c2):
        print("TRIANGULO ACUTANGULO")
    else:
        print("TRIANGULO OBTUSANGULO")
if a == b and b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")