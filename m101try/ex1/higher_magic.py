#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/19 17:42:19 by myohann-            #+#    #+#            #
#   Updated: 2026/08/20 13:32:05 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
from collections.abc import Callable


def ember(target: str, power: int) -> str:
    return f"Ember hit {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def gun(target: str, power: int) -> str:
    return f"Gun hit {target} for {power} HP"


def provoc(target: str, power: int) -> str:
    return (f"Provoc make {target} confused and hit "
            f"hit is_self {power} HP")


def snow(target: str, power: int) -> str:
    return f"snow hit {target} for {power} HP"


def mana(target: str, power: int, spell: Callable[[str, int], str]) -> bool:
    if target == "Dragon" and power < 20 and spell == ember:
        return False
    return True


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]) \
                    -> Callable[[str, int], tuple[str, str]]:
    return (lambda target, power: (spell1(target, power),
                                   spell2(target, power)))


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def in_amplified(target: str, power: int) -> str:
        p = power * multiplier
        resultat = base_spell(target, p)
        return resultat
    return in_amplified


def conditional_caster(condition: Callable[[str, int,
                                            Callable[[str, int], str]], bool],
                       spell: Callable[[str, int], str]) \
                        -> Callable[[str, int,
                                     Callable[[str, int], str]], str | Any]:
    def f_condition(target: str, power: int,
                    spells: Callable[[str, int], str]) -> str | Any:
        if condition(target, power, spells):
            return spell(target, power)
        return "Spell fizzled"
    return f_condition


def spell_sequence(spells: list[Callable[[str, int], str]]) \
        -> Callable[[str, int], list[str]]:
    def spell_lst(target: str, power: int) -> list[str]:
        lst_s = []
        for e in spells:
            lst_s.append(e(target, power))
        return lst_s
    return spell_lst


if __name__ == "__main__":
    try:
        test_values = [25, 9, 6]
        test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
        print("================================================")
        combine = spell_combiner(gun, provoc)
        print(f"Combined:  {combine('Dragon', 17)}")
        print("================================================")
        power = 9
        ampli = 5
        p_ampli = power_amplifier(snow, ampli)
        print(f"Original: {power}")
        print(f"amplify : {p_ampli('Knight', power)}")
        print("================================================")
        c_caster = conditional_caster(mana, ember)
        print(c_caster("Dragon", 19, ember))
        print(c_caster("Dragon", 20, ember))
        print("================================================")
        s_sequenc = spell_sequence([gun, ember, heal, snow, provoc])
        lst = s_sequenc("Goblin", 12)
        for i in lst:
            print(i)
    except Exception as e:
        print(e)
