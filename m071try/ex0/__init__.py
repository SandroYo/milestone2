#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   __init__.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/09 20:35:43 by myohann-            #+#    #+#            #
#   Updated: 2026/08/10 04:23:30 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .creature import FlameFactory, AquaFactory

__all__ = ["FlameFactory",
           "AquaFactory"]
