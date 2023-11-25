# Design a class:
#     1. Inserting a value (no duplicates)
#     2. Removing a value  
#     3. GetRandom a vlue that is already inserted (with equal probability)

import random as r
import os
class Store:
    def __init__(self):
        self.store = []
        
    def input(self):
        self.store.append(int(input("Insert a value: ")))

    def get_random(self):
        self.x = r.choice(self.store)
        print(self.x)
    def remove(self):
        self.remove_value = int(input("Insert value to remove: ")) 
        for value in self.store:

            if value == self.remove_value:
                self.store.remove(value)
            else:
                pass
    
    def print_list(self):
        print(self.store)

first_list = Store()
end_of_the_machine = True 

while end_of_the_machine:
    user_choice = input("what do you want ? \nInsert, Remove, Get_random\n")
    if user_choice == "end":
        os.system("cls")
        end_of_the_machine = False
    elif user_choice == "insert" or user_choice == "Insert":
        os.system("cls")
        first_list.input()
    elif user_choice == "Remove" or  user_choice == "remove":
        os.system("cls")
        first_list.remove()
    elif user_choice == "get_random" or  user_choice == "Get_random":
        os.system("cls")
        first_list.get_random()
    else:
        os.system("cls")
        user_choice = input("You wrote wrong, please type again\n Insert, Remove, Get_random\n")
    print(first_list.print_list())