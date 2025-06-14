class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name} - {self.age}"


if __name__ == "__main__":
    new_person = Person("John", 30)
    print(new_person)
