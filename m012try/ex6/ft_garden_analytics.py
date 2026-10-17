#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 20:09:36 by myohann-            #+#    #+#            #
#   Updated: 2026/07/03 20:56:45 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    class Stats:
        def __init__(self) -> None:
            self._G_var = 0
            self._A_var = 0
            self._S_var = 0
            self._P_var = 0

    def __init__(self, name: str, height: float, old: int):
        self.name = name
        self.stats = self.Stats()
        self.shade = False
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

    @staticmethod
    def is_year(age: int) -> bool:
        return age >= 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(self.name + f": {self._height:.1f}cm, {self._old} days old")
        self.stats._S_var += 1

    def grow(self) -> None:
        self._height += 2.1
        self.stats._G_var += 1

    def age(self) -> None:
        self._old += 1
        self.stats._A_var += 1


class Flower(Plant):
    def __init__(self, name: str, heigth: float, age: int, color: str):
        super().__init__(name, heigth, age)
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 n_seed: int):
        super().__init__(name, height, age, color)
        self.n_seed = n_seed

    def show(self) -> None:
        seed = 0
        Plant.show(self)
        print(" Color: " + self.color)
        if self.blooms is True:
            print(" Rose is blooming beautifully!")
            seed = self.n_seed
        else:
            print(" Rose has not bloomed yet")
        print(f" Seeds: {seed}")

    def bloom(self) -> None:
        self.blooms = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: float):
        super().__init__(name, height, age)
        self.trunk = trunk
        self.shade = True

    def show(self) -> None:
        Plant.show(self)
        print(f" Trunk diameter: {self.trunk:.1f}cm")

    def produce_shade(self) -> None:
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")
        self.stats._P_var += 1


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, season: str, nutritional: int):
        super().__init__(name, height, age)
        self.season = season
        self.nutritional = nutritional

    def show(self) -> None:
        Plant.show(self)
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.nutritional}")

    def grow(self) -> None:
        Plant.grow(self)
        Plant.age(self)
        self.nutritional += 1


def v_class(Plant: "Plant") -> None:
    print(f"Stats: {Plant.stats._G_var} grow", end="")
    print(f", {Plant.stats._A_var} age, {Plant.stats._S_var} show")
    if Plant.shade is True:
        print(f" {Plant.stats._P_var} shade")


if __name__ == "__main__":
    print(f"is 30 days more than a year? -> {Plant.is_year(30)}")
    print(f"is 400 days more than a year? -> {Plant.is_year(400)}")
    print("\n=== Garden Plant Types ===")
    print("=== Flower")
    plant1 = Flower("Rose", 25, 30, "red")
    plant1.show()
    v_class(plant1)
    plant1.grow()
    plant1.bloom()
    plant1.show()
    v_class(plant1)
    print("")
    print("=== Tree")
    plant2 = Tree("Oak", 200, 365, 5)
    plant2.show()
    v_class(plant2)
    plant2.produce_shade()
    v_class(plant2)
    print("")
    print("=== Seed")
    plant3 = Seed("Sunflower", 80, 45, "yellow", 42)
    plant3.show()
    v_class(plant3)
    plant3.age()
    plant3.grow()
    plant3.bloom()
    plant3.show()
    v_class(plant3)
    print("\n=== Anonymous")
    plant4 = Plant.anonymous()
    plant4.show()
    v_class(plant4)
