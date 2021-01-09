from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()


class Employee(Person):
    def __init__(self, first_name, last_name, date_of_birth, job):
        super().__init__(first_name, last_name, date_of_birth)
        self.job = job

    def __str__(self):
        return f"{self.fullname()} - {self.job}"


emp = Employee("João", "Rocha", datetime.now(), "Programmer")

print(emp)
print("is instance?", isinstance(emp, Person))
print("is subclass?", issubclass(Employee, Person))
