#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/16 21:27:48 by myohann-            #+#    #+#            #
#   Updated: 2026/07/17 10:49:10 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_command_request() -> None:
    len_param = len(sys.argv)
    print("Program name: ft_command_quest.py")
    if len_param != 1:
        print(f"Arguments received: {len_param - 1}")
        i = 1
        while len_param > i:
            print(f"Argument [{i}]: {sys.argv[i]}")
            i = i + 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len_param}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_request()
