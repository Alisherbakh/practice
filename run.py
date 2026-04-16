# Dunder __builtins__ , __init__
massage = "PYTHON: Everything is object"
print(massage)

result = type(massage)
print("result:", result)

''' in Python, there are bulitin tools:

(1) TYPES > int float str list dict
(2) Function > print(), len(), input(), type()
(3) CONSTANT > True False None
 
'''
print(dir(__builtins__))
