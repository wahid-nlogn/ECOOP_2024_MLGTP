class A:
    def f(self:Self, other:Self):
        return other.g(self)
    def g(self:Self, other:Self):
        return self.foo
    foo = 'bar'

class B(A):
    def f(self:Self, other:Self):
        return other.g(self)
    def g(self, other:Self):
        return other.baz
    baz = 'blah'
    foo = 'bar'

a = A()
b = B()

a.f(b)
