''' CLASS deep diving
    (1)ENCAPSULATION 
    (2)INHERITENCE <
    (3)POLIMORPHISM <
'''

print("==== INHERITENCE =====")
# PARENT > CHILD [only public & protected properties(state + method)]


class Animal():  # Parent

    description = " This class is parent for animals "

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes,I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----")
dog.make_voice()
fish.make_voice()

print("-------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog.status)
print("cat.status:", cat.status)
