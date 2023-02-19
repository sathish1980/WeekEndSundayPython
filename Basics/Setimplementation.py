class setimplementation():

    def setimplementations(self):
        fruits = {"apple", "orange", "banana", "pineapple", "apple", "grapes"}
        newfruits={"pomogranite","kiwi","mango"}
        print(type(fruits))
        print(fruits)
        for eachvalue in fruits:
            print(eachvalue)
        print(len(fruits))
        fruits.add("apple")
        print(fruits)
        fruits.update(newfruits)
        print(fruits)
        fruits.remove("banana")
        print(fruits)
        fruits.discard("oranges")
        print(fruits)
        fruits.pop()
        print(fruits)
        oldfruits=fruits.copy()
        print(oldfruits)
        fruits.clear()
        print(fruits)
        Store1 = {"apple", "orange", "banana", "pineapple", "apple", "grapes"}
        Store2 = {"apple", "orange", "banana", "kiwi"}
        #print(Store1.difference(Store2))
        #Store1.difference_update(Store2)
        #print(Store1.intersection(Store2))
        #Store1.intersection_update(Store2)
        print(Store1)
        print(Store1.issubset(Store2))
        print(Store1.issuperset(Store2))
        #newvar=Store1.symmetric_difference(Store2)
        #print(Store1.symmetric_difference_update(Store2))
        #Store1.symmetric_difference_update(Store2)
        #print(Store1)
        Store1.union(Store2)
        print(Store1)



obj = setimplementation()
obj.setimplementations()