#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 21:09:01 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:35:10 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    element = dark_spell_allowed_ingredients()
    for e in element:
        if ingredients.lower() in e.lower():
            return "VALID"
    return "INVALID"
