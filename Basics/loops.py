class loops:

    def __init__(self):
        print("i am constructor")

    def __init__(self,name):
        print("i am constructor", name)

    def whileloop(self,number):
        next10number=number+10
        while(number<next10number):
            print(number)
            number= number+2

    def forloop(self,number):
        next10number = number + 10
        fruits=["apple","orange","banana","kiwi","papaya"]
        for eachvale in fruits:
            if eachvale == "banana":
                #break
                continue
            print(eachvale)
        for eachvalue in range(number,next10number):
            print(eachvalue)

    def nestedforloop(self):
        fruits=["apple","orange","banana","kiwi","papaya"]
        month = ["january", "feb", "march", "april", "may"]
        for eachvale in fruits:

            if eachvale != "orange":
                print(eachvale)
                for eachmonth in month:
                    print(eachmonth)
    def div(self,a,b):
        try:
            c=a/b
            print(c)
            #ZeroDivisionError
        except ZeroDivisionError:
            print("you have entered zero value")
        except:
            print(Exception)
        finally:
            print("this is finally")

    def div2(self, a, b):
        c = a / b
        print(c)

obj=loops("sathish")
obj.div2(2,0)
obj.nestedforloop()

