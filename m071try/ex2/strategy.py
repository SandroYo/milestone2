#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategy.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 08:14:42 by myohann-            #+#    #+#            #
#   Updated: 2026/08/12 17:06:09 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex1.capacity import HealCapability, TransformCapability
from ex0.creature import Creature


class BattleStrategy(ABC):
    def __init__(self) -> None:
        self.strategy = "Normal"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.strategy = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise Exception("Only creature can fight"
                            " in this tornament")


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.strategy = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            if isinstance(creature, TransformCapability):
                print(creature.transform())
                print(creature.attack())
                print(creature.revert())
        else:
            raise Exception("Invalid Creature"
                            f" '{creature.__class__.__name__}'"
                            " for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.strategy = "Defensive"

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            if isinstance(creature, HealCapability):
                print(creature.attack())
                print(creature.heal())
        else:
            raise Exception("Invalid Creature "
                            f"'{creature.__class__.__name__}'"
                            " for this defensive strategy")
