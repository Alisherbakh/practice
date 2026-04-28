''' Packages &  Debugging
   (1) Python Packages &  Core Packages
   (2) Packages Manager & Exterel Packages
   (3) Debugging

'''
from PIL import Image
import turtle
print(" ======= Python Packages & Core Packages ======")
''' Python Packages/Modules: Core , File and External '''
# Core Packages > https://docs.python.org/3/library


# Core
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)
# turtle.done()

print("======")

my_file = open("material/massage.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()


# with = Context Manager automatic close()

with open("material/massage.txt") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)


print(" ======= Packages Manager & Exterel Packages ======")
# External Packages > https://pypi.org/
''' Package Manager >
   Python > pip pipenv
   NodeJS > npm yarn
   PHP > composer
   MacOS > brew

'''

with Image.open("material/tom3.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
