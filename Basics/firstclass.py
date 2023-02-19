"""print("sathish's")
print('kumar')"""
print("""sathish "kumar" R""")
print("""sathish "kumar" R
is a selnium
Tutor""")
print(2)
print("sathish kumar b.tech")

#function with out pameter with out return type
def add():
    print("addition")


#function with pameter
def addition(a,b):
    c = a + b
    d=multiply(a,b)
    print("addition" ,c)
    minus=c-d
    print(minus)
    print(multiply(a,b))

#function with pameter
def multiply(a,b):
    c = a * b
    return c

a=True
print(type(a))



add()
addition(15,20)