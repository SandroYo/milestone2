#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 23:24:53 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:34:02 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..elements import create_air
from ..potions import strength_potion
import elements


def lead_to_gold() -> str:
    return "Recipe transmuting Lead to Gold: "\
          f"brew {create_air()} and {strength_potion()} "\
          f"mixed with {elements.create_fire()}"
