#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/16 10:28:16 by myohann-            #+#    #+#            #
#   Updated: 2026/08/16 15:05:12 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import os


def check_envi() -> None:
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: you're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print()
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        v_py = f"/python{sys.version_info.major}.{sys.version_info.minor}"
        print(sys.prefix +
              "/lib" +
              v_py +
              "/site-packages")


if __name__ == "__main__":
    check_envi()
