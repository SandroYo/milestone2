#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_4.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 23:11:50 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 23:11:51 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy


print("=== Alembic 4 ===\n"
      "Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached\n"
      "This will raise an exception!\n"
      "Testing the hidden create_earth:"
      " Traceback (most recent call last):")
print(f"{alchemy.create_earth()}")
