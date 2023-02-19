class list:

    def listimplementation(self):
        fruits=["apple","orange","banana","pineapple","apple","grapes"]
        newfruits=["chiku","papaya"]
        print(fruits)
        print(type(fruits))
        for eacchvalue in fruits:
            print(eacchvalue)
        print(fruits[0:3])
        print(fruits[-2])
        fruits[1]="berry"
        print(fruits)
        fruits.insert(100,"watermelon")
        print(fruits)
        fruits.append("plums")
        print(fruits)
        print(len(fruits))
        fruits.insert(len(fruits), "new")
        print(fruits)
        fruits.extend(newfruits)
        print(fruits)
        fruits.remove("grapes")
        print(fruits)
        fruits.pop(1)
        print(fruits)
        fruits.pop()
        print(fruits)
        del fruits[5]
        print(fruits)
        beforecopy=fruits.copy()
        #del fruits
        fruits.clear()
        print(fruits)
        print(beforecopy)

obj=list()
obj.listimplementation()