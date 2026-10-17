#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/29 08:12:40 by myohann-            #+#    #+#            #
#   Updated: 2026/08/03 20:18:38 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.stock: list[Any] = []
        self.index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.stock:
            raise Exception("Empty storage!")
        else:
            tupl = (self.index, self.stock[self.index])
            self.index += 1
            return tupl


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, int) or isinstance(data, float):
            return True
        elif isinstance(data, list):
            for d in data:
                if isinstance(d, bool):
                    return False
                elif isinstance(d, list):
                    if self.validate(d) is False:
                        return False
                else:
                    if isinstance(d, int | float) is False:
                        return False
            return True
        return False

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if self.validate(data) is False:
            raise Exception(" Improper numeric data")
        else:
            if isinstance(data, list):
                for d in data:
                    self.ingest(d)
            else:
                self.stock.append(data)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for d in data:
                if isinstance(d, list):
                    if d == []:
                        return False
                    elif self.validate(d) is False:
                        return False
                elif isinstance(d, str) is False:
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise Exception(" Improper text data")
        else:
            if isinstance(data, list):
                for d in data:
                    self.ingest(d)
            else:
                self.stock.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(key, str) is False:
                    return False
                elif isinstance(value, str) is False:
                    return False
            return True
        if isinstance(data, list):
            for d in data:
                if self.validate(d) is False:
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise Exception(" Improper log data")
        else:
            if isinstance(data, list):
                for d in data:
                    self.ingest(d)
            else:
                buffer = []
                if isinstance(data, dict):
                    for value in list(data.values()):
                        buffer.append(value)
                    self.stock.append(buffer)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    data = 42
    print(f"Trying to validate input '{data}': {num.validate(data)}")
    print(f"Trying to validate input 'Hello': {num.validate('Hello')}")
    try:
        print("Test invalid ingestion of string 'foo'"
              " without prior validation:")
        num.ingest("foo")
    except Exception as error:
        print(f"Got exception: {error}")
    try:
        data_n = [1, 2, 3, 4, 5]
        print(f"Processing data: {data_n}")
        num.ingest(data_n)
        print("Extracting 3 values...")
        for a in [1, 2, 3]:
            tup = num.output()
            print(f"Numeric value {tup[0]}: {tup[1]}")
    except Exception as error:
        print(error)
    print("")
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    try:
        data_t = ['Hello', 'Nexus', 'World']
        print(f"Processing data: {data_t}")
        text.ingest(data_t)
        print("Extracting 1 value...")
        tup = text.output()
        print(f"Text value 0: {tup[1]}")
    except Exception as error:
        print(error)
    print("")
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    try:
        data_l = [{'log_level': 'NOTICE',
                  'log_message': 'Connection to server'},
                  {'log_level': 'ERROR',
                  'log_message': 'Unauthorized access!!'},]
        print(f"Processing data: {data_l}")
        log.ingest(data_l)
        print("Extracting 2 values...")
        for a in [1, 2,]:
            tup = log.output()
            dic = tup[1]
            log_tup = ""
            for d in dic:
                log_tup += ": " + d
            print(f"Log entry {tup[0]}{log_tup}")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
