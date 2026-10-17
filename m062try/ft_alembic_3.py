#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_3.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 04:00:25 by myohann-            #+#    #+#            #
#   Updated: 2026/08/05 04:00:35 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_air


print("=== Alembic 3 ===\n"
      "Accessing alchemy/elements.py "
      "using 'from ... import ...' structure")
print(f"Testing create_air: {create_air()}")
