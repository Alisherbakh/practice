''' Tuples
   (1) What is tuples: type vs list
   (2) Unpacking arguments
   (3) zip

'''

print("===== What is tuples: type vs list ======")
# Java/PHP/NodeJS array => Python list

# literal
numbs = [3, 5, 1, 2]


# constructor
letter = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruit:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"

# try avoid this
people = "Andrew", "John"
animals = "dog",

print("===== Unpacking arguments ======")

group = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = group
print(f"the x: {x} and y: {y}")
print("z:", z)  # list

# *args > tuple


def calculate(*args):
    print("args:", args)
    total = 1
    for x in args:
        total *= 1
        print(f"the total value: {total}")
        return total


# call
calculate(1, 7, 2, 3)
print("-----")
calculate(0, 2, 300)
print("------")
calculate(5, 7)

print("-------")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type (**kwargs) value: {type(kwargs)}")
    print(f" Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


# CALL
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)
