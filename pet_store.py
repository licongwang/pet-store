""" this program runs a simulation of a pet store, 
    allowing customers to store their pets
"""
import argparse
import random

PET_TYPE = ["Dog", "Cat"]


class Animal(object):
    """The class of Animal, all living creatures belong to here.

    Attributes:
        name: A string of the name of an animal
        type: A string of the type of an animal
        is_pet: A boolean indicating whether the animal is a pet
        health: A integer between 70-100, the health of the animal
    """

    def __init__(self, name, type, pet_health=random.randint(70, 100)):
        """initialize Animal with given arguments"""
        self.name = name
        self.type = type
        self.is_pet = type in PET_TYPE
        self.health = pet_health

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
    def __init__(self, f):
        """initialize Store"""
        self.customer_pet = {}

        f.seek(0)
        lines = list(f)
        for line in lines:
            customer_name, pet_name, pet_type, pet_health = line.split()
            animal_to_store = Animal(pet_name, pet_type, pet_health)
            self.store_pet(customer_name, animal_to_store)

    def store_pet(self, customer, animal):
        """storing a pet for a customer, a customer may have many pets
        
        Args:
            customer: A string indicating the customer's name.
            animal: An Animal class instance which is to be stored
        
        Returns:
            True or False depending on whether the given 
            animal is a pet.
        """
        if not animal.is_pet:
            return False
        else:
            if customer not in self.customer_pet:
                self.customer_pet[customer] = []
            self.customer_pet[customer] += [animal]
            return True

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
    """store or check pets for a customer"""

    # initialize the store
    f = open("store_info.txt", "a+")
    my_store = Store(f)

    # parsing command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("customer_name", help="name of the customer, assume unique")
    parser.add_argument("action", help="action to perform, e.g. 'store', 'check'")
    parser.add_argument("pet_name", nargs='?', help="name of the pet")
    parser.add_argument("pet_type", nargs='?', help="type of the pet")
    args = parser.parse_args()

    customer_name = args.customer_name
    pet_name = args.pet_name
    pet_type = args.pet_type
    action = args.action

    # perform command line action
    if action == "store":
        animal_to_store = Animal(pet_name, pet_type)

        # store succeeded
        if my_store.store_pet(customer_name, animal_to_store):
            f.write(customer_name + " " + pet_name + " " + pet_type + " " +
                    str(animal_to_store.health) + "\n")
            print("store completed, customer: " + customer_name + ", pet name: "
                  + pet_name + ", type: " + pet_type)
        # store failed
        else:
            print("store failed, only a pet can be stored, " + pet_type + " is not a pet")

    elif action == "check":
        my_store.check_pet(customer_name)
    else:
        print("invalid action: " + action)

    f.close()

if __name__ == "__main__":
    main()

