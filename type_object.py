

class A(object):
    pass

class B(A):
    pass

a = A()
print(a.__str__())

o = object()
print(o)

print(isinstance(A, object))
print(isinstance(int, object))

print(dir(o))
o1 = object()
o2 = object()

# print(o1 > o2)

# o1.__gt__()

class C:
    def my_gt(self):
        raise TypeError('my_gt not supported')

class D(C):

    def my_gt(self):
        raise TypeError('my_gt not supported')

    # def __gt__(self, other):
    #     return 5

c = C()
#c.my_gt()
d1 = D()
d2 = D()
print(d1 > d2)


