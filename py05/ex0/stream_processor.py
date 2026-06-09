#!/usr/bin/env python3

from abc import ABC, abstractmethod

from typing import Any, List, Union


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for
                                              x in data)

    def process(self, data: List[Union[int, float]]) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        count = len(data)
        total = sum(data)
        avg = total / count if count > 0 else 0
        return f"Processed {count} numeric values, sum={total}, avg={avg:.1f}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        char = len(data)
        words = len(data.split())
        return f"Processed text: {char} characters, {words} words"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and any(level in data for level in
                                             ["ERROR", "INFO", "DEBUG"])

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        level = data.split(":")[0]
        message = data.split(":")[1].strip() if ":" in data else data
        tag = "[ALERT]" if "ERROR" in level else "[INFO]"
        return f"{tag} {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        base_format = super().format_output(result)
        return base_format


def run_system():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    try:
        print("Initializing Numeric Processor...")

        num_proc = NumericProcessor()
        num_data = [1, 2, 3, 4, 5]

        print(f"Processing data {num_data}")

        if num_proc.validate(num_data):
            print("Validation: Numeric data verified")
            print(num_proc.format_output(num_proc.process(num_data)))

        print("\nInitializing Text Processor...")

        txt_proc = TextProcessor()
        txt_data = "Hello Nexus World"

        print(f'Processing data: "{txt_data}"')

        if txt_proc.validate(txt_data):
            print("Validation: Text data verified")
            print(txt_proc.format_output(txt_proc.process(txt_data)))

        print("\nInitializing Log Processor...")

        log_proc = LogProcessor()
        log_data = "ERROR: Connection timeout"

        print(f'Processing data: "{log_data}"')

        if log_proc.validate(log_data):
            print("Validation: Log entry verified")
            print(log_proc.format_output(log_proc.process(log_data)))

        print("\n=== Polymorphic Processing Demo ===")
        print("\nProcessing multiple data types through same interface...")

        processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(),
                                           LogProcessor()]

        payloads: List[Any] = [[1, 2, 3], "Python Power", "INFO: System ready"]

        for i, (proc, data) in enumerate(zip(processors, payloads), 1):
            result = proc.process(data)
            print(f"Result {i}: {result}")

    except Exception as e:
        print(f"Critical system error: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    run_system()
