class Dictonary():

    def dictonaryimplementation(self):
        name="sathish"
        student={"name":"sathish","age":25,"Gender":"Male"}
        print(type(student))
        print(student.get("Name"))
        print(student.keys())
        for eachvalue in student.keys():
            print(eachvalue)
            print(student.get(eachvalue))
        print(student.values())
        print(len(student))
        print(student.items())
        student["Genders"]="Female"
        print(student)
        student.update({"Genders":"Trans"})
        print(student)
        student.pop("Genders")
        print(student)
        student.popitem()
        print(student)
        #del student
        newstud=student.copy()
        student.clear()
        print(newstud)
        print(student)

obj = Dictonary()
obj.dictonaryimplementation()
