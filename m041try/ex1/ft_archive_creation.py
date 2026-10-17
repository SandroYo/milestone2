#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/24 21:57:43 by myohann-            #+#    #+#            #
#   Updated: 2026/07/27 20:08:00 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_as_cat(file_name: str) -> str | None:
    file = None
    content = ""
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
    if file is None:
        return file
    return content


def ft_restorer(content: str) -> str:
    new_contents = ""
    print("Transform data:")
    contents = content.split("\n")
    for str in contents:
        new_contents = new_contents + str + "#\n"
    print("---")
    print("")
    print(new_contents, end="")
    print("")
    print("---")
    return new_contents


def ft_creat_file(file_name: str, content: str) -> None:
    file = None
    try:
        file = open(file_name, "w")
        print(f"Saving data to '{file_name}'")
        file.write(content)
        print(f"Data saved in file '{file_name}'.")
    except OSError:
        print("Not saving data.")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        content = ft_as_cat(sys.argv[1])
        if content is not None:
            new_content = ft_restorer(content)
            try:
                file_name = input("Enter new file name (or empty): ")
                ft_creat_file(file_name, new_content)
            except (KeyboardInterrupt, EOFError) as error:
                print(error)
    else:
        print("Usage: ft_ancient_text.py <file>")
