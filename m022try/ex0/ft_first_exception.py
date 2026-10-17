#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 19:11:37 by myohann-            #+#    #+#            #
#   Updated: 2026/07/13 09:11:11 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    v1 = "25"
    v2 = None
    print("=== Garden Temperature ===")
    print(f"\nInput data is '{v1}'")
    try:
        print(F"Temperature is now {input_temperature(v1)}°C")
    except ValueError as error:
        print(error)
    print(f"\nInput data is '{v2}'")
    try:
        print(f"Temperature is now {input_temperature(v2)}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
