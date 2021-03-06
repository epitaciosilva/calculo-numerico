import math

def simpson13(f, x0, xn, n):
    h = float(xn - x0) / n

    r = f(x0) + f(xn)

    for i in range(1,n):
        k = x0 + i*h

        if i%2 == 0:
            r = r + 2 * f(k)
        else:
            r = r + 4 * f(k)

    r = r * float(h/3)

    return r

def simpson38(f, x0, xn, n ): 
    h = float(xn - x0)/n
    r = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i*h

        if (i % 3 == 0): 
            r = r + 2 * f(k) 
        else: 
            r = r + 3 * f(k) 
      
    r = float((3*h)/8) * r

    return r

def trapezioComposto(f, a, b, n):
    h = float(b - a)/n
    r = 0
    r += f(a)
    for i in range(1, n):
        r += f(a + i*h)*2.0
    r += f(b)
    
    return r*(h/2.0)

if __name__ == "__main__":
    f = lambda x: math.sin(x)*x

    x0 = -5; xn = 5
    for k in range(1, 7):
        print('k: ' + str(k))
        m = 6*k
        print('m: ' + str(m))
        print('Trapezio composto:')
        print(trapezioComposto(f, x0, xn, m))
        m = 3*k
        print('m: ' + str(m))
        print('Simpson 1/3:')
        print(simpson13(f, x0, xn, m))
        m = 2*k
        print('m: ' + str(m))
        print('Simpson 3/8:')
        print(simpson38(f, x0, xn, m))
