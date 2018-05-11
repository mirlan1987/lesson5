class Car: 
    def__init__(self,name,type,age):
        self.name = name
        self.type = type
        self.age = age

    def__repr__(self):
        return"This car's name is (name),type is (type), an is (age) years old",format(
								name=self.name
								type=self.type
								age=self.age)
    @staticmethod
    def pip ():
        return "PIP!!!"
mersedes =  Car("mersedes","s-class","4")
print (mersedes)
print(mersedes,pip)
