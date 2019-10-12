a = 1
b = 1

def f():
    global a, b
    a = a + b
    a, b = b, a
    return a


def tower():
    n = int(input())
    a = list(range(1, n+1))
    b = []
    c = []
    print(a, b, c)

    if (n % 2 ==1):
        for i in range (int(n/2)):
            buf=a.pop(-1)
            c.append(buf)

            buf = a.pop(-1)
            b.append(buf)

            buf = b.pop(-1)
            c.append(buf)

            print("1-3\n1-2\n2-3")

        buf = a.pop(-1)
        c.append(buf)
        print ("1-3")
    else:
        for i in range(int(n/2)):
            buf=a.pop(-1)
            b.append(buf)

            buf = a.pop(-1)
            c.append(buf)

            buf = b.pop(-1)
            c.append(buf)

            print("1-2\n1-3\n2-3")

    print(a, b, c)

print(f(),' ',f(),' ',f(),' ',f(),' ',f(),' ')
tower()