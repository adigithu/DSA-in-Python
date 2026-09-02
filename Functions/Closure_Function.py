x=88
def f1():
    x=80
    def f2():
        print(x)
    return f2
result=f1()
result()