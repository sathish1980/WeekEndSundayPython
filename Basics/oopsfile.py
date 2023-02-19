class firstclass():
    global a
    a=100
    def add(self):
        a=10
        name='sathish'
        a=67
        print("addition",str(self.a))

    def addition(self,a, b):
        c = a + b
        d = one.multiply(a, b)
        print("addition", c)
        minus = c - d
        print(minus)
        print(one.multiply(a, b))

    # function with pameter
    def multiply(self,a, b):
        c = a * b
        return c

    def anotherfun(self):
        a=45
        print(a)

one=firstclass()
one.add()