#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/17 10:27:23 by myohann-            #+#    #+#            #
#   Updated: 2026/07/23 22:47:57 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_score_analytics() -> None:
    len_param = len(sys.argv)
    if len_param != 1:
        n_lst = []
        i = 1
        n_player = 0
        while i < len_param:
            try:
                n_lst.append(int(sys.argv[i]))
                n_player = n_player + 1
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i = i + 1
        if n_lst == []:
            print("No scores provided. Usage: python3"
                  " ft_score_analytics.py <score1> <score2> ...")
        else:
            print(f"Scores processed: {n_lst}")
            print(f"Total players: {n_player}")
            print(f"Total score: {sum(n_lst)}")
            print(f"Average score: {(sum(n_lst) / n_player):.2f}")
            print(f"High score:  {max(n_lst)}")
            print(f"Low score: {min(n_lst)}")
            print(f"Score range: {max(n_lst) - min(n_lst)}")
    else:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
