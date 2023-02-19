class testfile():

    def textfileread(self):

        file=open("C:\\Users\\sathishkumar\\PycharmProjects\\weekendSunday\\input\\sample.txt","r")
        writefile=open("C:\\Users\\sathishkumar\\PycharmProjects\\weekendSunday\\input\\output.txt","w")
        #print(file.read())
        #print(file.readline())
        #print(file.readline())
        #print(file.readlines())
        alllines = file.readlines()
        writefile.write("This is entred automatically")

        for eachstring in alllines:
            print(eachstring)
            emptystring="";
            if eachstring.__contains__("sathish"):
                allvalue=eachstring.split(" ")
                for eachval in allvalue:
                    str(eachval).replace("sathish","n",1)
                    emptystring=emptystring+eachval;
                writefile.write(str(emptystring))
                pass
            else:
                writefile.write(str(eachstring))
        print("Write comlpeted")

obj = testfile()
obj.textfileread()
