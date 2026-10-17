#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/19 22:36:39 by myohann-            #+#    #+#            #
#   Updated: 2026/07/20 17:28:00 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def gen_player_achivements() -> set["str"]:
    achivements = {"Crafting Genius", "Strategist", "World Savior",
                   "Speed Runner", "Survivor", "Master Explorer",
                   "Treasure Hunter", "Unstoppable", "First Steps",
                   "Collector Supreme", "Untouchable", "Sharp Mind",
                   "Boss Slayer", "Hidden Path Finder"}
    n_achiv = random.randint(1, 8)
    p_achiv = set(random.sample(list(achivements), n_achiv))
    return (p_achiv)


def test_p_achivement() -> None:
    achivements = {"Crafting Genius", "Strategist", "World Savior",
                   "Speed Runner", "Survivor", "Master Explorer",
                   "Treasure Hunter", "Unstoppable", "First Steps",
                   "Collector Supreme", "Untouchable", "Sharp Mind",
                   "Boss Slayer", "Hidden Path Finder"}
    Alice = gen_player_achivements()
    Bob = gen_player_achivements()
    Charlie = gen_player_achivements()
    Dylan = gen_player_achivements()
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print("")
    print("All distinct achievements: "
          f"{set.union(Alice, Bob, Charlie, Dylan)}")
    print("")
    print("Common achievements: "
          f"{set.intersection(Alice, Bob, Charlie, Dylan)}/n")
    print("")
    print(f"Only Alice has: {set.difference(Alice, Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {set.difference(Bob, Charlie, Dylan, Alice)}")
    print(f"Only Charlie has: {set.difference(Charlie, Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {set.difference(Dylan, Alice, Bob, Charlie)}")
    print("")
    print(f"Alice is missing: {set.difference(achivements, Alice)}")
    print(f"Bob is missing: {set.difference(achivements, Bob)}")
    print(f"Charlie is missing: {set.difference(achivements, Charlie)}")
    print(f"Dylan is missing: {set.difference(achivements, Dylan)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    test_p_achivement()
