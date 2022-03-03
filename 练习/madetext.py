# encoding= utf-8
def foo():
    while True:
        res=yield 4
        print("res:",res)
g=foo()
print(next(g))
print(g.send(7))