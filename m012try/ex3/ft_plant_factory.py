#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 20:09:03 by myohann-            #+#    #+#            #
#   Updated: 2026/06/23 20:09:04 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, old: int):
        self.name = name
        self.height = height
        self.old = old

    def show(self) -> None:
        print(self.name + f": {self.height:.1f}cm, {self.old} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.old += 1


if __name__ == "__main__":
    print("=== Garden Plant Output ===")
    x = range(1, 8)
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    print("Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()
