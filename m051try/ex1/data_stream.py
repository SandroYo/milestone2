#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/29 20:43:13 by myohann-            #+#    #+#            #
#   Updated: 2026/08/03 22:04:46 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.stock: list[Any] = []
        self.index = 0
        self.count = 0
        self.remain = 0

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

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise Exception(" Improper numeric data")
        else:
            if isinstance(data, list):
                for d in data:
                    self.ingest(d)
            else:
                self.stock.append(data)
                self.count += 1


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
                self.count += 1


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
                    self.count += 1


class DataStream:
    def __init__(self) -> None:
        self.proc_stock: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.proc_stock.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for s in stream:
            check = False
            try:
                for proce in self.proc_stock:
                    if proce.validate(s):
                        proce.ingest(s)
                        check = True
                        break
                if check is False:
                    print("DataStream error - "
                          f"Can't process element in stream: {s}")
            except Exception as e:
                print(e)

    def print_processors_stats(self) -> None:
        if self.proc_stock:
            for proc in self.proc_stock:
                if isinstance(proc, NumericProcessor):
                    print(f"Numeric Processor: total {proc.count} items"
                          " processed, remaining"
                          f" {proc.count - proc.index} on processor")
                elif isinstance(proc, TextProcessor):
                    print(f"Text Processor: total {proc.count} items"
                          " processed, remaining"
                          f" {proc.count - proc.index} on processor")
                elif isinstance(proc, LogProcessor):
                    print(f"Log Processor: total {proc.count} items processed,"
                          f" remaining {proc.count - proc.index} on processor")
        else:
            print("No processor found, no data")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    stremer = DataStream()
    print("== DataStream statistics ==")
    stremer.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    num = NumericProcessor()
    stremer.register_processor(num)
    print()
    data = ['Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42,
            ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    stremer.process_stream(data)
    print("== DataStream statistics ==")
    stremer.print_processors_stats()
    print()
    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stremer.register_processor(text)
    stremer.register_processor(log)
    print("Send the same batch again")
    stremer.process_stream(data)
    print("== DataStream statistics ==")
    stremer.print_processors_stats()
    print()
    print("Consume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    try:
        for i in range(0, 3):
            if i < num.count:
                num.output()
        for i in range(1, 3):
            if i < num.count:
                text.output()
        log.output()
    except Exception as e:
        print(e)
    print("== DataStream statistics ==")
    stremer.print_processors_stats()


if __name__ == "__main__":
    main()
