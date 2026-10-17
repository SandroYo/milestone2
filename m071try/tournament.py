#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 15:51:54 by myohann-            #+#    #+#            #
#   Updated: 2026/08/12 18:50:05 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex2 import AggressiveStrategy, NormalStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy
from ex0 import FlameFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capacity import HealCapability, TransformCapability


def get_Cname(creature: Creature) -> str:
    if isinstance(creature, Creature):
        if isinstance(creature, HealCapability):
            return "Healing"
        if isinstance(creature, TransformCapability):
            return "Transform"
        return creature.__class__.__name__


def init_name(opponement: list[tuple[Creature, BattleStrategy]]) -> str:
    i = 0
    popup = ""
    popup += " [ "
    while i < len(opponement):
        crea = opponement[i]
        popup += (
                 f"({get_Cname(crea[0])}"
                 + "+" +
                 f"{crea[1].strategy})"
        )
        if i < len(opponement) - 1:
            popup += ", "
        i += 1
    popup += " ]"
    return popup


def battle(opponement: list[tuple[Creature, BattleStrategy]]) -> None:
    print(init_name(opponement))
    print("*** Tournament ***")
    print(f"{len(opponement)} opponents involved")
    i = 0
    while i < len(opponement):
        j = i + 1
        while j < len(opponement):
            if i != j:
                print()
                print("* Battle *")
                op1 = opponement[i]
                op2 = opponement[j]
                print(op1[0].describe())
                print("vs.")
                print(op2[0].describe())
                print("  now fight!")
                op1[1].act(op1[0])
                op2[1].act(op2[0])
            j += 1
        i += 1


if __name__ == "__main__":
    try:
        print("Tournament 0 (basic)")
        f_fac = FlameFactory()
        h_fac = HealingCreatureFactory()
        op1 = f_fac.create_base()
        op2 = h_fac.create_base()
        A_st = AggressiveStrategy()
        D_st = DefensiveStrategy()
        N_st = NormalStrategy()
        grp = [(op1, N_st), (op2, D_st)]
        battle(grp)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")
    try:
        print()
        print("Tournament 1 (error)")
        grp = [(op1, A_st), (op2, D_st)]
        battle(grp)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")
    try:
        print()
        print("Tournament 2 (multiple)")
        t_fac = TransformCreatureFactory()
        op3 = t_fac.create_base()
        grp = [(op1, N_st), (op2, D_st),
               (op3, A_st)]
        battle(grp)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")
