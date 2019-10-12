a=1
b=1

def f():
    global a, b
    a = a + b
    a, b = b, a
    return a

print(f(),' ',f(),' ',f(),' ',f(),' ',f(),' ')