#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 19:11:43 by myohann-            #+#    #+#            #
#   Updated: 2026/07/09 19:11:44 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    t_str = int(temp_str)
    if t_str > 0 and t_str < 40:
        return t_str
    else:
        if t_str < 0:
            raise ValueError(f"{t_str}°C is too cold for plants (min 0°C)")
        else:
            raise ValueError(f"{t_str}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
    v1 = "25"
    v2 = "abc"
    v4 = "100"
    v5 = "-50"
    print("=== Garden Temperature ===")
    for a in (v1, v2, v4, v5):
        print(f"\nInput data is '{a}'")
        try:
            print(F"Temperature is now {input_temperature(a)}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
