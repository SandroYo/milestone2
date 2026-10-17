#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 19:11:59 by myohann-            #+#    #+#            #
#   Updated: 2026/07/09 21:18:44 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def test_error() -> None:
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as a:
        print(f"Caught PlantError: {a}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as a:
        print(f"Caught WaterError: {a}")


def test_i_error() -> None:
    print("\nTesting catching all garden errors...")
    try:
        raise GardenError
    except GardenError as a:
        print(f"Caught GardenError: {a}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as a:
        print(f"Caught GardenError: {a}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_error()
    test_i_error()
    print("\nAll custom error types work correctly!")
