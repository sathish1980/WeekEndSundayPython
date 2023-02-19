from Basics.Besanttechnology import Besanttechnology
from Basics.Courses import courses


class batches(courses,Besanttechnology):

    def WeekdayBatch(self):
        Weekdays=["Mon","tue","wed","thur","fri"]
        timing=["10-11","11-12","7-8","6-7"]
        print(Weekdays)
        for eachtimg in timing:
            print(eachtimg)

    def WeekendBatch(self):
        Weekend=["sat","sun"]
        timing=["10-11","11-12","7-8"]
        print(Weekend)
        for eachtimg in timing:
            print(eachtimg)
    def Batchopted(self,option):
        if option =="weekday":
            self.WeekdayBatch()
        elif option == "weekend":
            self.WeekendBatch()
        else:
            print("incorrectbatch mode")
obj=batches()
obj.besant_info("chennai")
obj.course()
obj.Batchopted("weekday")
#obj.WeekendBatch()
#obj.WeekdayBatch()