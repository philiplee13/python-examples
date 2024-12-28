from meal import MealBuilder, MealDirector


def main():
    # so this is one way - without using perhaps a la carte
    # meal = Meal()
    # meal.build_side("Sprite")
    # meal.build_entree("Chicken")
    # meal.get_meal()

    # using director - so maybe preset options
    builder = MealBuilder()
    director = MealDirector(builder)
    option_1 = director.build_meal(1)
    option_2 = director.build_meal(2)
    if option_1:
        option_1.get_meal()  # for some reason if we don't check if it's an instantied first
        # pylint complains
        # prob a setting
        #
    if option_2:
        option_2.get_meal()


if __name__ == "__main__":
    main()
