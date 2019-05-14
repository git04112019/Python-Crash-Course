# Class

# Create class


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend class


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user object
vinh = User('Vinh Hoang', 'vinh@gmail.com', 30)
print(vinh.name)
print(type(vinh))

print(vinh.greeting())

vinh.has_birthday()
print(vinh.greeting())

# Init customer object
janet = Customer('Janet', 'janet@gmail.com', 30)
print(janet.greeting())
janet.set_balance(500)
print(janet.greeting())
