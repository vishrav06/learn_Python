class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum =0
        for i in self.marks:
            sum+= i
        avg = sum/3
        print(self.name)
        print(avg)

    @staticmethod
    def hello():
        print("Helllo")



s1 = Student("Avi", [34, 65, 75])
s1.get_avg()
s1.hello()
