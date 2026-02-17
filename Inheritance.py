class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.behaviour = "friendly"
    def speak(self):
        super().speak()
        print(f"{self.name} barks. He is very {self.behaviour}")

animal = Animal("Generic Animal")
animal.speak()

dog = Dog("buddy", "Golden Retriever")
dog.speak()