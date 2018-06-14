""" this program runs a simulation of a pet store, 
    allowing customers to store their pets
"""
import argparse
import random

pet_type = ["Dog", "Cat"]


class Animal(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_pet = type in pet_type
        self.health = random.randint(80, 100)

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
                print("pet name: " + pet.name + ", type: " + pet.type + ", health: " + str(pet.health))

my_store = Store()

# parsing command line argument
parser = argparse.ArgumentParser()
parser.add_argument("customer_name", help="name of the customer, assume unique")
parser.add_argument("action", help="action to perform, e.g. 'store', 'check'")
parser.add_argument("pet_name", nargs='?', help="name of the pet")
parser.add_argument("pet_type", nargs='?', help="type of the pet")
args = parser.parse_args()

customer_name = args.customer_name

# manually stored pet to test "check"
myPet = Animal("frog", "Dog")
my_store.customer_pet[customer_name] = [myPet]

# perform command line action
if args.action == "store":
    animal_to_store = Animal(args.pet_name, args.pet_type)
    my_store.store_pet(customer_name, animal_to_store)
elif args.action == "check":
    my_store.check_pet(customer_name)
else:
    print("invalid action: " + args.action)

