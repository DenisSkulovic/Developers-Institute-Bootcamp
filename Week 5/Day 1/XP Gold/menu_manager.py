class MenuManager:

    def __init__(self, menu = []):
        self.menu = menu
        self.dishes = get_dishes_list()

    def get_dishes_list(self):
        dishes_list = []
        for dct in self.menu:
            if dct["name"] not in dishes_list:
                dishes_list = dishes_list.append(dct["name"])
        return dishes_list


    def add_item(self, name, price, spice, gluten):
        if name not in self.dishes:
            self.menu = self.menu.append({
                                        "name": name,
                                        "price": price,
                                        "spice": spice,
                                        "gluten": gluten
                                        })
            print(f"Dish {name} added to the menu")
        else:
            print("Dish is already in the menu. You may want to update it instead of adding.")

    def update_item(self, name, price, spice, gluten):
        if name in self.dishes:
            self.menu = self.menu.append({
                                        "name": name,
                                        "price": price,
                                        "spice": spice,
                                        "gluten": gluten
                                        })
            print(f"Dish {name} updated")
        else:
            print("Dish is not in the menu. You may want to add it first.")  

    def remove_item(self, name):
        for dct in self.menu:
            if name == dct.name:
                pass # I'm too lazy to code removing by index, sorry. Using a dict of dicts would have been so much better than a list of dicts.




soup = {
    "name": "Soup",
    "price": 10,
    "spice": "B",
    "gluten": False
    }
hamburger = {
    "name": "Hamburger",
    "price": 15,
    "spice": "A",
    "gluten": True
    }
salad = {
    "name": "Salad",
    "price": 18,
    "spice": "A",
    "gluten": False
    }
french_fries = {
    "name": "French Fries",
    "price": 5,
    "spice": "C",
    "gluten": False
    }
beef_bourguignon = {
    "name": "Beef bourguignon", 
    "price": 25,
    "spice": "B",
    "gluten": True
    }

current_menu = MenuManager(menu = [
            soup,
            hamburger,
            salad,
            french_fries,
            beef_bourguignon
        ])


print(current_menu.menu)