#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 23:22:31 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:28:01 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .elements import create_earth, create_air
import elements


def healing_potion() -> str:
    return ("Healing potion brewed with"
            f" {create_earth()} and {create_air()}")


def strength_potion() -> str:
    return ("Strength potion brewed with"
            f" {elements.create_fire()} and {elements.create_water()}")
