#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/09 20:40:15 by myohann-            #+#    #+#            #
#   Updated: 2026/08/12 19:39:37 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import FlameFactory, AquaFactory
from ex0.creature import CreatureFactory


def Testing_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def Testing_battle(f_fac: CreatureFactory, w_fac: CreatureFactory) -> None:
    Flameling = f_fac.create_base()
    Aquabub = w_fac.create_base()
    print(Flameling.describe())
    print("vs.")
    print(Aquabub.describe())
    print(Flameling.attack())
    print(Aquabub.attack())


if __name__ == "__main__":
    try:
        print("Testing factory")
        Testing_factory(FlameFactory())
        print()
        print("Testing factory")
        Testing_factory(AquaFactory())
        print()
        print("Testing battle")
        Testing_battle(FlameFactory(), AquaFactory())
    except Exception as e:
        print(e)
