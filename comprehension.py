''' Comprehension
   (1) What is comprehension & list comp
   (2) set and dictionary comp.

'''

print("===== What is comprehension & list comprehension =======")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
   a) *iterable
   b) <expression> for item in iterable
   c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 3, 2, 3, 20]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


print("===========")
people = [("Robert", 21), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version
print("list_numbers:", list_people)

print("=====")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)


print("===== set and dictionary comprehension =======")

numb = [1, 2, 3, 2, 3, 20]
set_numbs = {*numb}
print("set_numbs:", set_numbs)  # a version

dict_people = {person[0]: person[1] for person in people}  # b version
print("dict_people:", dict_people)


dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # c version
print("dict_people2:", dict_people2)

# (<expression> for item in iterable) generic
