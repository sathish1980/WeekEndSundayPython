class Tuple():

    def Tupleimplementation(self):
        fruits = ("apple", "orange", "banana", "pineapple", "apple", "grapes")
        print(type(fruits))
        for eachvalue in fruits:
            print(eachvalue)
        for eachvalue in range(0,len(fruits)):
            print(fruits[eachvalue])
        print(fruits[0])
        print(len(fruits))
        if "apple" in fruits:
            print("Yes")
        print(fruits.index("banana"))
        print(fruits.count("grape"))
        del fruits

obj = Tuple()
obj.Tupleimplementation()