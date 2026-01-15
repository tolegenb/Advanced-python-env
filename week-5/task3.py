class Person:
    def __init__(self, name):
        self._name = name  # encapsulation

    def get_info(self):
        return f"Person name: {self._name}"


class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def get_info(self):  # polymorphism
        return f"Student name: {self._name}, University: {self.university}"


person = Person("Arman")
student = Student("Aruzhan", "AITU")

print(person.get_info())
print(student.get_info())
