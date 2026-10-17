#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_spellbook.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 21:08:28 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:34:38 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients) == "VALID":
        return (f"Spell recorder {spell_name}"
                f"({ingredients}) - VALID")
    return f"Spell rejected {spell_name} - INVALID"
