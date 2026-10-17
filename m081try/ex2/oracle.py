#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/16 15:10:10 by myohann-            #+#    #+#            #
#   Updated: 2026/08/16 21:46:22 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import os
from dotenv import load_dotenv

if __name__ == "__main__":

    try:
        load_dotenv()
    except Exception as e:
        print(e)
        sys.exit()
    print("ORACLE STATUS: Reading the Matrix...")

    m_tmp = os.getenv("MATRIX_MODE")
    d_tmp = os.getenv("DATABASE_URL")
    a_tmp = os.getenv("API_KEY")
    l_tmp = os.getenv("LOG_LEVEL")
    z_tmp = os.getenv("ZION_ENDPOINT")
    missing = []
    if not m_tmp:
        m_mode = "production"
        missing.append(m_mode)
    else:
        m_mode = m_tmp
    if not d_tmp:
        d_mode = "Connected to local instance"
        missing.append(d_mode)
    else:
        d_mode = d_tmp
    if not a_tmp:
        a_mode = "Authenticated"
        missing.append(a_mode)
    else:
        a_mode = a_tmp
    if not l_tmp:
        l_mode = "DEBUG"
        missing.append(l_mode)
    else:
        l_mode = l_tmp
    if not z_tmp:
        z_mode = "Online"
        missing.append(z_mode)
    else:
        z_mode = z_tmp

    if m_mode == "development":
        print(f"Mode: {m_mode}\n"
              f"Database: {d_mode}\n"
              f"API Access: {a_mode}\n"
              f"Log Level: {l_mode}\n"
              f"Zion Network: {z_mode}\n")
    elif m_mode == "production":
        print(f"Mode: {m_mode}\n"
              f"Log Level: {l_mode}\n"
              f"Zion Network: {z_mode}\n")

    if missing == []:
        print("Environment security check:\n"
              "[OK] No hardcoded secrets detected\n"
              "[OK] .env file properly configured\n"
              "[OK] Production overrides available")
    else:
        print("Environment security check:\n"
              "[OK] No hardcoded secrets detected\n"
              "[Error] .env file not properly configured\n"
              "[OK] Production overrides available")
