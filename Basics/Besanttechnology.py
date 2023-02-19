class Besanttechnology():

    def besant_info(self,location):
        print("welcom to Besant technology")
        if location == "chennai":
            self.besant_Chennai_Branches()
        elif location == "bangalore":
            self.besant_Bangalore_Branches()
        else:
            print("please provide the valida location")

    def besant_Chennai_Branches(self):
        branches=["Annanagar","Tnagar","Velachery","Tambaram"]
        for eachbracn in branches:
            print(eachbracn)

    def besant_Bangalore_Branches(self):
        branches=["Marathali","Indranagar","jaya nagar",]
        for eachbracn in branches:
            print(eachbracn)


