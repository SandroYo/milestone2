#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacity.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 00:02:24 by myohann-            #+#    #+#            #
#   Updated: 2026/08/10 08:09:58 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.creature import Creature, CreatureFactory
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", " Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.morph = False

    def attack(self) -> str:
        if self.morph:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        if not self.morph:
            self.morph = True
            return "Shiftling shifts into a sharper form!"
        return "Shiftling is already into a sharper form!"

    def revert(self) -> str:
        if self.morph:
            self.morph = False
            return "Shiftling returns to normal."
        return "Shiftling is already to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.morph = False

    def attack(self) -> str:
        if self.morph:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        if not self.morph:
            self.morph = True
            return "Morphagon morphs into a dragonic battle form!"
        return "Morphagon is already into a dragonic battle form!"

    def revert(self) -> str:
        if self.morph:
            self.morph = False
            return "Morphagon stabilizes its form."
        return "Morphagon has already stabilized its form."


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
