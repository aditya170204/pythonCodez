# class Car:
#     color='blue'
#     model=' BMW M5'
    
# c1=Car
# print(c1.model,'in',c1.color,)



class Student:
    # DEFAULT CONSTRUCTORS
    def __init__(self):
            
        pass
        
    #PARAMETERIZED CONSTRUCTORS
    def __init__(self,fullname,marks):
        self.name=fullname    
        self.marks=marks    

        print("New admissions added ")
    
s1=Student('Rajji',69)
print(s1.name,s1.marks)
s2=Student('Raunak',88)
print(s2.name,s2.marks)
    
class Dost:
    def __init__(self,name,how,city):
        self.name=name
        self.how=how
        self.city=city
    def batao(self):
        print(f"my frnd's name is {self.name} he became my frnd in {self.how} and he's from {self.city}")
d1=Dost("alok","family meetup","darbhnga")
d2=Dost("chacha","chatt","drbnga")
d3=Dost("rajji","college","Gola,Jharkhand")

d1.batao()
d2.batao()
d3.batao()