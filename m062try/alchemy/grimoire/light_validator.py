#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 20:52:16 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:35:40 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    element = light_spell_allowed_ingredients()
    for e in element:
        if ingredients.lower() in e.lower():
            return "VALID"
    return "INVALID"
