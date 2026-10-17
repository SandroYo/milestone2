#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 21:23:55 by myohann-            #+#    #+#            #
#   Updated: 2026/07/23 22:41:39 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def gen_lst_dico() -> None:
    players_name = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                    'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players_name}")
    first_lst = [lst.capitalize() for lst in players_name]
    print(f"New list with all names capitalized: {first_lst}")
    second_lst = [lst for lst in players_name if lst == lst.capitalize()]
    print(f"New list of capitalized names only: {second_lst}\n")
    NC_dico = {lst: random.randint(1, 1000) for lst in first_lst}
    print(f"Score dict: {NC_dico}")
    ave_score = sum(NC_dico.values()) / len(NC_dico)
    print(f"Score average is {ave_score:.2f}")
    HS_dico = {lst: NC_dico[lst] for lst in NC_dico
               if NC_dico[lst] > ave_score}
    print(f"High scores: {HS_dico}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    gen_lst_dico()
