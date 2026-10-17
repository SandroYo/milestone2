#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 20:18:01 by myohann-            #+#    #+#            #
#   Updated: 2026/07/24 21:54:06 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_as_cat(file_name: str) -> None:
    file = None
    try:
        print(f"Accessing file '{file_name}'")
        file = open(file_name, "r")
        content = file.read()
        print("---")
        print("")
        print(content)
        print("")
        print("---")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if file:
            file.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_as_cat(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")
