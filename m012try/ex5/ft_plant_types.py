#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 20:09:29 by myohann-            #+#    #+#            #
#   Updated: 2026/07/03 20:52:29 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, old: int):
        self.name = name
        if height < 0:
            print("Rose: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if old < 0:
            print("Rose: Error, age can't be negative")
            self._old = 0
        else:
            self._old = old

    def show(self) -> None:
        print(self.name + f": {self._height:.1f}cm, {self._old} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Rose: Error, height can't be negative")
            print("Height update rejected")
        else:
            print(f"Height updated: {height}cm")
            self._height = height

    def set_age(self, old: int) -> None:
        if old < 0:
            print("Rose: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {old} days")
            self._old = old

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._old

    def grow(self) -> None:
        self._height += 2.1

    def age(self) -> None:
        self._old += 1


class Flower(Plant):
    def __init__(self, name: str, heigth: float, old: int, color: str):
        super().__init__(name, heigth, old)
        self.color = color
        self.blooms = False

    def show(self) -> None:
        Plant.show(self)
        print(" Color: " + self.color)
        if self.blooms is True:
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")

    def bloom(self) -> None:
        self.blooms = True


class Tree(Plant):
    def __init__(self, name: str, height: float, old: int, trunk: float):
        super().__init__(name, height, old)
        self.trunk = trunk

    def show(self) -> None:
        Plant.show(self)
        print(f" Trunk diameter: {self.trunk:.1f}cm")

    def produce_shade(self) -> None:
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 old: int, season: str, nutritional: int):
        super().__init__(name, height, old)
        self.season = season
        self.nutritional = nutritional

    def show(self) -> None:
        Plant.show(self)
        print(f" Harvest season: {self.season}")
        print(f" Nutritional value: {self.nutritional}")

    def grow(self) -> None:
        Plant.grow(self)
        Plant.age(self)
        self.nutritional += 1


if __name__ == "__main__":
    x = range(1, 21)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1 = Flower("Rose", 25, 30, "red")
    plant1.show()
    plant1.bloom()
    plant1.show()
    print("")
    print("=== Tree")
    plant2 = Tree("Oak", 200, 365, 5)
    plant2.show()
    plant2.produce_shade()
    print("")
    print("=== Vegetable")
    plant3 = Vegetable("Tomato", 5, 10, "April", 0)
    plant3.show()
    for i in x:
        plant3.grow()
    plant3.show()
