#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/20 06:56:34 by myohann-            #+#    #+#            #
#   Updated: 2026/08/20 14:48:41 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    elif operation == 'add':
        return reduce(add, spells)
    elif operation == 'multiply':
        return reduce(mul, spells)
    elif operation == 'max':
        return reduce(max, spells)
    elif operation == 'min':
        return reduce(min, spells)
    else:
        raise Exception(f"Unknown operator: '{operation}'")


def base_enchantment(power: int, element: str, target: str) -> str:
    return (f"'{element}' enchantment on '{target}' with {power} power.")


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    darkness = partial(base_enchantment, 50, 'Darkness')
    chain_explosion = partial(base_enchantment, 50, 'Chain explosion')
    vampirism = partial(base_enchantment, 50, 'Vampirism')
    return {
        'darkness': darkness,
        'chain_explosion': chain_explosion,
        'vampirism': vampirism
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell_system(spell: Any) -> str:
        return ("Unknown spell type.")

    @spell_system.register(int)
    def _(spell: int) -> str:
        return (f"{spell} damage")

    @spell_system.register(str)
    def _(spell: str) -> str:
        return (spell)

    @spell_system.register(list)
    def _(spell: list[Any]) -> str:
        return (f"{len(spell)} spells")
    return spell_system


if __name__ == "__main__":
    print("==========================================")
    print("Testing spell reducer...")
    try:
        my_list = [86, 67, 60, 69]
        addition = spell_reducer(my_list, 'add')
        print("Sum:", addition)
        multiplication = spell_reducer(my_list, 'multiply')
        print("Product", multiplication)
        find_max = spell_reducer(my_list, 'max')
        print("Max", find_max)
        find_min = spell_reducer(my_list, 'min')
        print("Min", find_min)
        unknown_operator = spell_reducer(my_list, 'square_root')
        print("Square root:", unknown_operator)
    except Exception as e:
        print(e)

    print()
    print("==========================================")
    print("Testing partial enchanter...")
    try:
        test = partial_enchanter(base_enchantment)
        print(test['darkness']('Deep Dark Blade'))
        print(test['chain_explosion']('Crossbow'))
        print(test['vampirism']('Katana'))
    except Exception as e:
        print(e)

    print()
    print("==========================================")
    print("Testing memoized fibonacci...")
    try:
        index_list = [0, 1, 3, 5, 10, 15]
        for n in index_list:
            fib_test = memoized_fibonacci(n)
            print(memoized_fibonacci.cache_info())
            print(f"Fib({n}): {fib_test}")
    except Exception as e:
        print(e)

    print()
    print("==========================================")
    print("Testing spell dispatcher...")
    try:
        dispatch = spell_dispatcher()
        print("Damage spell:", dispatch(42))
        print("Enchantment:", dispatch('fireball'))
        print("Multi-cast:", dispatch(['fireball', 'heal', 'shield']))
        print(dispatch({'power': 100}))
    except Exception as e:
        print(e)
