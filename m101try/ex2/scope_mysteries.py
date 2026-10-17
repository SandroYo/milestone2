#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/20 01:20:42 by myohann-            #+#    #+#            #
#   Updated: 2026/08/20 14:01:55 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def self_counter() -> int:
        nonlocal count
        count += 1
        return count
    return self_counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    current_power = initial_power

    def accumul(amount: int) -> int:
        nonlocal current_power
        current_power += amount
        return current_power
    return accumul


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def spe_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return spe_enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault = {}

    def store(key: str, value: int) -> None:
        vault[key] = value

    def recall(key: str) -> int | str:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall
        }


if __name__ == "__main__":
    print("Testing mage counter...")
    mage1 = mage_counter()
    print(f"counter_a call 1: {mage1()}")
    print(f"counter_a call 2: {mage1()}")
    mage2 = mage_counter()
    print(f"counter_b call 1: {mage2()}\n")
    print("==========================================")
    print("Testing spell accumulator...")
    accumul1 = spell_accumulator(100)
    print(f"Base 100, add 20: {accumul1(20)}")
    print(f"Base 100, add 30: {accumul1(30)}")
    print("==========================================")
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print("==========================================")
    print("Testing memory vault...")
    storage = memory_vault()
    storage['store']('secret', 42)
    recall = storage['recall']('secret')
    recall1 = storage['recall']('unknown')
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall}")
    print(f"Recall 'unknown': {recall1}")
