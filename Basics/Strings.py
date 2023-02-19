class strings:

    def stringimplementaion(self):
        name=" sathish kumar R is a tutor "
        name1="new satring name is sathish"
        filename="sathish.txts"
        print(name)
        print(len(name))
        print(name[1])
        for eachval in range(0,len(name)):
            print(name[eachval])
        for eachval in name:
            print(eachval)
        print("tutors" not in name)
        print(name[1:6])
        print(name.upper())
        print(name.lower())
        print(name.capitalize())
        print(name.isalnum())
        newsteing=name.replace(" ", "")
        print(name.replace(" ",""))
        print(name.replace("sathis", "A"))
        print(newsteing.isalpha())
        print(name.strip())
        print(name.lstrip())
        print(name.rstrip())
        print(name.split("s"))
        print(name+name1)
        institure= "besant \"Technology\" in chennai"
        print(institure)
        print(name.startswith(" sathish"))
        print(name.endswith("R"))
        print(filename.rfind("s"))


obj=strings()
obj.stringimplementaion()