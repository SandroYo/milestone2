#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 21:57:37 by myohann-            #+#    #+#            #
#   Updated: 2026/07/23 21:23:03 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    name = ['Bob', 'Alice', 'Dylan', 'Charlie']
    actions = ['run', 'eat', 'sleep', 'grap',
               'move', 'swim', 'climb', 'release']
    pack = (random.choice(name), random.choice(actions))
    yield pack


def consume_event(lst_event: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    to_del = random.choice(lst_event)
    lst_event.remove(to_del)
    yield to_del


if __name__ == "__main__":
    for i in range(1000):
        gen = gen_event()
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    lst_event = []
    for i in range(10):
        gen = gen_event()
        lst_event.append(next(gen))
    print(f"Built list of 10 events: {lst_event}")
    for i in range(10):
        gen = consume_event(lst_event)
        print(f"Got event from list: {next(gen)}")
        print(f"Remains in list: {lst_event}")
