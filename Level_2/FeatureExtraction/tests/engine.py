class Engine:
    def subscribe(self:Self, f:Function(DynParameters, Dyn)):
        print (42)

engine = Engine()
if True:
    de = engine
else:
    de = False

def m(x,y):
    pass

x = de.subscribe
x(m)
