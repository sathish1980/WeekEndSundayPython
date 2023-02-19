class conditions():

    def trafficsignal(self,color,vehicle,Status):
        if color == "Red":
            if (vehicle =="Ambulance" or vehicle !="Ambulance") and Status =="Empty":
                print("Please stop")
                print("Dont blow horn")
            else:
                print("Please give  a  way")
        elif color =="Orange":
            print("you can about  to start ")
        elif color == "Green":
            pass
        else:
            print("this is incorrect color")

    def age(self,ageval):
        if ageval>18:
            print("you are major")
        elif ageval<=18:
            print("you are minor")
obj=conditions()
obj.trafficsignal("Orange","bike","notEmpty")
obj.age(21)