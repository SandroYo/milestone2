#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_0.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 23:12:01 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:12:02 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import potions


if __name__ == "__main__":
    print("=== Distillation 0 ===\n"
          "Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}")
