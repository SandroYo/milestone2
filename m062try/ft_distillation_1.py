#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_1.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 23:12:15 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:12:16 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===\n"
          "Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")
