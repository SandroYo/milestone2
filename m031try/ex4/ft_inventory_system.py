#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/20 21:20:10 by myohann-            #+#    #+#            #
#   Updated: 2026/07/23 22:51:12 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def is_syntax(s: str) -> None:
    tmp = tuple(s)
    if tmp[0] == ':' or tmp[len(tmp) - 1] == ':':
        raise IndexError
    else:
        i = 0
        while i < len(tmp):
            if tmp[i] == " ":
                raise IndexError
            i += 1


def ft_max(stock: list[int]) -> int:
    i = 0
    while i < (len(stock)):
        j = 0
        while stock[i] >= stock[j]:
            if j == (len(stock) - 1):
                return i
            j += 1
        i += 1
    return i


def ft_min(stock: list[int]) -> int:
    i = 0
    while i < (len(stock)):
        j = 0
        while stock[i] <= stock[j]:
            if j == (len(stock) - 1):
                return i
            j += 1
        i += 1
    return i


def ft_parse_in() -> None:
    inventory = {}
    items = []
    stockage = []
    for arg in sys.argv[1:]:
        try:
            is_syntax(arg)
            enter = arg.split(':', 1)
            name = str(enter[0])
            nb = int(enter[1])
            if name in inventory:
                print(f"Redundant item '{name}' - discarding")
            else:
                inventory[name] = nb
                items.append(name)
                stockage.append(nb)
        except IndexError:
            print(f"Error - invalid parameter '{arg}'")
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(stockage)} items: {sum(stockage)}")
    for key in items:
        print(f"Item {key} represents "
              f"{((inventory[key] / sum(stockage)) * 100):.1f}%")
    if len(inventory) != 0:
        print(f"Item most abundant: {items[ft_max(stockage)]}"
              f" with quantity {stockage[ft_max(stockage)]}")
        print(f"Item most abundant: {items[ft_min(stockage)]}"
              f"with quantity {stockage[ft_min(stockage)]}")
    else:
        print("Item most abundant: None with quantity 0")
        print("Item most abundant: None with quantity 0")
    inventory['magic_item'] = 1
    print(inventory)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_parse_in()
