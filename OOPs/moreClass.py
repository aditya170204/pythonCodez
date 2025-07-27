class Student:
    def __init__(self,nickname:str,sch:str,age:int):
        self.nickname=nickname
        self.sch=sch
        self.age=age
    def detail(self):
         print(f"student's nickname is {self.nickname} he/she is {self.age} years old and studies in {self.sch} school ")
    

s1=Student('aadi','woodbine',"ed")
s1.detail()
