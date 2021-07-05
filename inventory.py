def nLists(lists):
    """Assign and print numerical values to items in a list"""
    for list in lists:
        print(f"{lists.index(list)+1}. {list}")


# define the inventory lists and print them in numerical lists
weapon = ["blaster", "knife"]
consumable = ["water", "oxygen tank", "first aid kit"]
protection = ["space suit", "tent"]
print("Available weapons:")
nLists(weapon)
print("Available consumables:")
nLists(consumable)
print("Available protection:")
nLists(protection)
