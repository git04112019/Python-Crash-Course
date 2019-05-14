
# String Formatting & Methods
# Lists: ordered, changeable, allows duplicate members

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get len
print(len(fruits))

# Append to Lít
fruits.append('Mangos')
print(fruits)

# Remove from Lít
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Change value
fruits[0] = 'Blueberries'
print(fruits)

# Tuples: ordered, unchanngeable, allows duplicate members

# Create tuple
fruits_tuple = ('Apples', 'Oranges', 'Grapes')
print(fruits_tuple)

# Single value needs trailing comma
fruits_tuple_2 = ('Apples',)

# Get value
print(fruits_tuple[1])

# Can't change value
# fruits_tuple[0] = 'New'

# Del tuple
del fruits_tuple_2

# Get length
print(len(fruits_tuple))

# Set: unordered, unindexed, no duplicate members

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Add duplicate
fruits_set.add('Apples')
print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete
del fruits_set

# Dictionaries: unordered, changeable, indexed, no duplicate members

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person)

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')
print(person2)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict key
print(person.keys())

# Get items
print(person.items())

# Copy dict
person2 = person.copy()
print(person2)
person2['city'] = 'New York'
print(person2)

# Remove item
del(person['age'])
print(person)

person.pop('phone')
print(person)

# Get length
print(len(person2))

# Clear
person.clear()
print(person)

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 20}
]

print(people)

print(people[1]['name'])

# Functions

# Create function


def sayHello(name):
    print(f'Hello {name}')


sayHello('John Snow')

# Return values


def getSum(num1, num2):
    total = num1 + num2
    return total


print(getSum(10, 20))


# Lambda function: similar to JS arrow functions

# getSum= lambda num1, num2: num1 + num2


print(getSum(10, 3))


# Conditionals

x = 10
y = 5

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')


# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# and, or, not
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

if not (x == y):
    print(f'{x} is not equal to {y}')

# Membership operatos: not, not in, is, is not

numbers = [1, 2, 3, 4, 5]
if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)

# Loops
# Modules
# Classes & Objects
# Working With Files
# Working With JSON
