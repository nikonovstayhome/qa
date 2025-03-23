class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def __eq__(self, other):
        raise NotImplementedError

