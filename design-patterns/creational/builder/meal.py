class MealBuilder:
    def __init__(self):
        self.drink: str | None = None
        self.entree: str | None = None
        self.side: str | None = None
        self.dessert: str | None = None

    def build_drink(self, drink: str):
        self.drink = drink
        return self

    def build_entree(self, entree: str):
        self.entree = entree
        return self

    def build_side(self, side: str):
        self.side = side
        return self

    def build_dessert(self, dessert: str):
        self.dessert = dessert
        return self

    def get_meal(self):
        print(f"Your meal contains the following...")
        if self.drink:
            print(f"Drink is {self.drink}")
        if self.entree:
            print(f"Entree is {self.entree}")
        if self.side:
            print(f"Side is {self.side}")
        if self.dessert:
            print(f"Dessert is {self.dessert}")


class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_meal(self, options: int):
        if options == 1:
            return (
                self.builder.build_drink("Sprite")
                .build_entree("Chicken")
                .build_side("Chips")
                .build_dessert("Vanilla Ice Cream")
            )
        elif options == 2:
            return (
                self.builder.build_drink("Coke")
                .build_entree("Beef")
                .build_side("Salad")
                .build_dessert("Cake")
            )
