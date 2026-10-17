#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/19 15:12:01 by myohann-            #+#    #+#            #
#   Updated: 2026/08/20 13:18:12 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int)\
        -> list[dict[str, Any]]:
    return list(filter(lambda power: power['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    p_max = max(mages, key=lambda a: a["power"])
    p_min = min(mages, key=lambda a: a["power"])
    a_pow = list(map(lambda a: a['power'], mages))
    a_ver = sum(a_pow) / len(a_pow)
    return {'max_power': p_max['power'], 'min_power': p_min['power'],
            'avg_power': (round(a_ver, 2))}


if __name__ == "__main__":
    print(artifact_sorter([{'name': 'Water Chalice', 'power': 119,
                            'type': 'focus'},
                           {'name': 'Water Chalice', 'power': 101,
                            'type': 'focus'},
                           {'name': 'Crystal Orb', 'power': 77,
                            'type': 'accessory'},
                           {'name': 'Ice Wand', 'power': 93,
                            'type': 'weapon'}]))
    mages = [{'name': 'Casey', 'power': 68, 'element': 'ice'},
             {'name': 'Zara', 'power': 56, 'element': 'earth'},
             {'name': 'River', 'power': 64, 'element': 'light'},
             {'name': 'Casey', 'power': 80, 'element': 'shadow'},
             {'name': 'Zara', 'power': 94, 'element': 'lightning'}]
    print()
    print(power_filter(mages, 70))
    print()
    spells = ['heal', 'meteor', 'tornado', 'flash']
    print(spell_transformer(spells))
    print()
    print(mage_stats(mages))
