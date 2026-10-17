#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/17 11:20:22 by myohann-            #+#    #+#            #
#   Updated: 2026/07/21 21:03:14 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def ft_len_input(lst: list[str]) -> int:
    nb: int = 0
    for i in lst:
        i += i
        nb += 1
    return nb


def get_player_pos() -> None:
    retri = 1
    print("Get a first set of coordinates")
    while retri > 0:
        try:
            enter = (input("Enter new coordinates as"
                           " floats in format 'x,y,z': ")).split(',')
            if ft_len_input(enter) != 3:
                raise ValueError
            x1 = float(enter[0])
            y1 = float(enter[1])
            z1 = float(enter[2])
            first_pos = (x1, y1, z1)
            print(f"Got a first tuple: {first_pos}")
            retri = 0
            print(f"It includes: X={x1}, Y={y1}, Z={z1}")
            distance = math.sqrt((0-x1)**2 + (0-y1)**2 + (0-z1)**2)
            print(f"Distance to center: {distance:.4f}")
        except ValueError:
            print("Invalid syntax")
        except KeyboardInterrupt:
            print("")
        except EOFError:
            print("")
    print("\nGet a second set of coordinates")
    while retri == 0:
        try:
            enter = (input("Enter new coordinates as "
                           "floats in format 'x,y,z': ")).split(',')
            if ft_len_input(enter) != 3:
                raise IndexError
            err = enter[0]
            x2 = float(enter[0])
            err = enter[1]
            y2 = float(enter[1])
            err = enter[2]
            z2 = float(enter[2])
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            print(f"Distance between the 2 sets of coordinates: "
                  f"{distance:.4f}")
            retri = 1
        except IndexError:
            print("Invalid syntax")
        except ValueError as error:
            print(f"Error on parameter '{err}': {error}")
        except KeyboardInterrupt:
            print("")
        except EOFError:
            print("")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
