class AllStaff:
    def __init__(self, name, age, id, birthdate,job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

class Management(AllStaff):
    def car(self):
        print(self.car())
