#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/27 12:49:49 by myohann-            #+#    #+#            #
#   Updated: 2026/07/27 15:37:47 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def secure_archive(file_name: str, use:
                   str, w_conten: str = "") -> tuple[bool, str]:
    try:
        if use == "r":
            with open(file_name, use) as file:
                content = file.read()
            result = (True, content)
        elif use == "w":
            with open(file_name, use) as file:
                file.write(w_conten)
            result = (True, "Content successfully written to file")
        else:
            raise OSError("Not a open fonction")
    except OSError as error:
        result = (False, F"{error}")
    return result


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print("")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test.txt", "r"))
    print("")
    print("Using 'secure_archive' to read from a regular file:")
    prev_conten = secure_archive("txt.txt", "r")
    print(prev_conten)
    print("")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("text.txt", "w", prev_conten[1]))
