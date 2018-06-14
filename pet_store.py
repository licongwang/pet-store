""" this program runs a simulation of a pet store, 
    allowing customers to store their pets
"""

pet_type = ["Dog", "Cat"]


class Animal(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_pet = type in pet_type

    def shout(self):
        if self.type == "Cat":
            print("Meow~")
        elif self.type == "Dog":
            print("Woof!")
        elif self.type == "Horse":
            print("Neigh~")
        else:
            print("???")


class Store(object):
    def __init__(self):
        self.customer_pet = {}

    # storing a pet for a customer, a customer may have many pets
    def store_pet(self, customer, animal):
        if not animal.is_pet:
            print("store failed, only a pet can be stored, " + animal.type + " is not a pet")
        else:
            if customer not in self.customer_pet:
                self.customer_pet[customer] = []
            self.customer_pet[customer] += [animal]

            print("store completed, customer: " + customer + ", pet Name: " + animal.name + ", type: " + animal.type)

    # allows a customer to check his/her pets stored
    def check_pet(self, customer):
        if customer not in self.customer_pet:
            print(customer + " doesn't have pets stored")
        else:
            print(customer + " has:")
            for pet in self.customer_pet[customer]:
                print("pet name: " + pet.name + ", type: " + pet.type)

my_store = Store()
my_pet = Animal("frog", "Dog")
my_animal = Animal("piggy", "Horse")
my_store.store_pet("licong", my_pet)
my_store.store_pet("licong", my_animal)

