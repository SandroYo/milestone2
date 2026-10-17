#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/04 19:31:59 by myohann-            #+#    #+#            #
#   Updated: 2026/06/30 19:25:00 by myohann-           ###   ########.fr      #
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
    print("=== Garden Plant Growth ===")
    x = range(1, 8)
    plant1 = Plant("Rose", 25, 30)
    nb = plant1.height
    plant1.show()
    for i in x:
        plant1.height = round(plant1.height, 1)
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print(f"Growth this week: {round(plant1.height - nb, 1)}cm")
