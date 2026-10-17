#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/16 11:10:30 by myohann-            #+#    #+#            #
#   Updated: 2026/08/16 15:04:40 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from importlib.util import find_spec
from importlib.metadata import version


def check_pack() -> bool:
    lst_pack: dict[str, str] = {"pandas": "Data manipulation ready",
                                "numpy": "Numerical computation ready",
                                "matplotlib": " Visualization ready"}
    dependece = True
    for element in lst_pack:
        if find_spec(element):
            print(f"[OK] {element} ({version(element)})"
                  f"  - {lst_pack[element]}")
        else:
            print(f"WARNING : Missing {element}")
            print(f"Please : pip install {element}")
            print("or")
            print(f"poetry add {element}")
            print()
            print()
            dependece = False
    return dependece


def loader_matrix() -> None:
    import pandas
    import numpy
    from matplotlib import pyplot
    x = numpy.arange(42)
    y = x + 3**2
    try:
        data = (pandas.DataFrame({'time': x, 'value': y}))
        print("Start !")
        pyplot.plot(data['time'], data['value'], color='green')
        pyplot.title("Matrix data")
        pyplot.xlabel("time (secondes)")
        print("Loading ...")
        pyplot.ylabel("value (nb)")
        pyplot.savefig("matrix_data.png")
        print("program complete")
    except Exception as e:
        print(e)
    finally:
        pyplot.close()


def diff_pip_poetry() -> None:
    print("\n=== 'pip' vs 'poetry' ===\n")
    print("pip -> requirements.txt")
    print("Install -> pip install -r requirements.txt")
    print("\npoetry -> pyproject.toml")
    print("Install -> poetry install")


if __name__ == "__main__":
    if check_pack():
        loader_matrix()
    else:
        print("Can't load matrix without all ressources")
    diff_pip_poetry()
