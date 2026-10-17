#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_spellbook.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 20:47:46 by myohann-            #+#    #+#            #
#   Updated: 2026/08/09 21:20:04 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    if validate_ingredients(ingredients) == "VALID":
        return (f"Spell recorder {spell_name}"
                f"({ingredients}) - VALID")
    print(validate_ingredients(ingredients))
    return f"Spell rejected {spell_name} - INVALID"

def test():
    print(validate_ingrediens)
