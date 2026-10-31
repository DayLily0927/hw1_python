class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender}")
class Student(Person):
    def __init__(self,name,age,gender,college,classnum):
        super().__init__(name,age,gender)
        self.college=college
        self.classnum=classnum
    def personInfo(self):
        super().personInfo()
        print(f"college:{self.college},class:{self.classnum}")
    def __str__(self):
        return f"name:{self.name},age:{self.age},gender:{self.gender},college:{self.college},class:{self.classnum}"