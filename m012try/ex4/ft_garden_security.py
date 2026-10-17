#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 20:09:11 by myohann-            #+#    #+#            #
#   Updated: 2026/06/30 19:41:22 by myohann-           ###   ########.fr      #
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

    def get_age(self) -> int:
        return self._old

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._old += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", -1, -10)
    plant1.show()
    plant1 = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    plant1.show()
    print("")
    plant1.set_height(25)
    plant1.set_age(30)
    print("")
    plant1.set_height(-1)
    plant1.set_age(-1)
    print("")
    print("Current state: ", end="")
    plant1.show()
