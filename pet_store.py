""" this program runs a simulation of a pet store, 
    allowing customers to store their pets
"""
import argparse
import random

PET_TYPE = ["Dog", "Cat"]


class Animal(object):
    """The class of Animal, all living creatures belong to here.

    Attributes:
        name: A string of the name of a animal
        type: A string of the type of a animal
        is_pet: A boolean indicating whether the animal is a pet
        health: A integer between 70-100, the health of the animal
    """

    def __init__(self, name, type):
        """initialize Animal with given arguments"""
        self.name = name
        self.type = type
        self.is_pet = type in pet_type
        self.health = random.randint(70, 100)

    def shout(self):
        """the animal talks depends on its type."""
        if self.type == "Cat":
            print("Meow~")
        elif self.type == "Dog":
            print("Woof!")
        elif self.type == "Horse":
            print("Neigh~")
        else:
            print("???")


class Store(object):
    """The class of the pet store, customers can store their pets here.

    Attributes:
        customer_pet: A dictionary, keys(string): customer names, 
            values(Animal class instance): pets stored by the customer
    """
    def __init__(self):
        """initialize Store"""
        self.customer_pet = {}

    def store_pet(self, customer, animal):
        """storing a pet for a customer, a customer may have many pets
        
        Args:
            customer: A string indicating the customer's name.
            animal: An Animal class instance which is to be stored
        
        Outputs:
            Success or failure message depending on whether the given 
            animal is a pet, since only pets can be stored.
        """
        if not animal.is_pet:
            print("store failed, only a pet can be stored, " + animal.type + " is not a pet")
        else:
            if customer not in self.customer_pet:
                self.customer_pet[customer] = []
            self.customer_pet[customer] += [animal]

            print("store completed, customer: " + customer + ", pet Name: " + animal.name + ", type: " + animal.type)

    def check_pet(self, customer):
        """allows a customer to check his/her pets stored
        Args:
            customer: A string indicating the customer's name.
        
        Outputs:
            A list of all pets owned by the customer, or a message 
            indicating the customer did not store any pets
        """
        if customer not in self.customer_pet:
            print(customer + " doesn't have pets stored")
        else:
            print(customer + " has:")
            for pet in self.customer_pet[customer]:
                print("pet name: " + pet.name + ", type: " + pet.type + ", health: " + str(pet.health))


def main():
    my_store = Store()

    # parsing command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("customer_name", help="name of the customer, assume unique")
    parser.add_argument("action", help="action to perform, e.g. 'store', 'check'")
    parser.add_argument("pet_name", nargs='?', help="name of the pet")
    parser.add_argument("pet_type", nargs='?', help="type of the pet")
    args = parser.parse_args()

    customer_name = args.customer_name

    # perform command line action
    if args.action == "store":
        animal_to_store = Animal(args.pet_name, args.pet_type)
        my_store.store_pet(customer_name, animal_to_store)
    elif args.action == "check":
        my_store.check_pet(customer_name)
    else:
        print("invalid action: " + args.action)


if __name__ == "__main__":
    main()

