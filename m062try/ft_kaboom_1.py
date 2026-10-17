#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/05 21:31:11 by myohann-            #+#    #+#            #
#   Updated: 2026/08/09 19:38:52 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.grimoire.dark_spellbook


def secret_import() -> None:
    print("=== Kaboom 1 ===\n"
          "Access to alchemy/grimoire/dark_spellbook.py directly\n"
          "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(alchemy.grimoire.dark_spellbook.
          dark_spell_record("mind_control", "arsenic"))


if __name__ == "__main__":
    secret_import()
