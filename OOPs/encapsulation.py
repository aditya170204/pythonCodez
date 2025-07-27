class Party:
    def __init__(self,food,drink):
        self.food=food
        self.__drink=drink
    def beverage(self,bever):
        self.__drink+=bever
    def get_bottles(self):
        
        return self.__drink
    def foods(self):
        return self.food
p1=Party("pizza","whiskey")
p1.beverage("scotch")
print(p1.get_bottles())
print(p1.foods())