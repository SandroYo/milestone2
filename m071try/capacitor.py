#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 07:45:58 by myohann-            #+#    #+#            #
#   Updated: 2026/08/12 19:38:34 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("  base:")
    h_fac = HealingCreatureFactory()
    sprotling = h_fac.create_base()
    print(sprotling.describe())
    print(sprotling.attack())
    print(sprotling.heal())
    print("  evolved:")
    bloo = h_fac.create_evolved()
    print(bloo.describe())
    print(bloo.attack())
    print(bloo.heal())
    print()
    print("Testing Creature with transform capability")
    print("  base:")
    t_fac = TransformCreatureFactory()
    shi = t_fac.create_base()
    print(shi.describe())
    print(shi.attack())
    print(shi.transform())
    print(shi.attack())
    print(shi.revert())
    print("  evolved:")
    mor = t_fac.create_evolved()
    print(mor.describe())
    print(mor.attack())
    print(mor.transform())
    print(mor.attack())
    print(mor.revert())
