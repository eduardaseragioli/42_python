from abc import ABC, abstractmethod
from typing import Any


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
        if not isinstance(data, list):
            return False
        for item in data:
            if not isinstance(item, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Numeric data verification failed")
        count = len(data)
        total = sum(data)
        if count > 0:
            average = total / count
        else:
            average = 0.0
        result = f"Processed {count} numeric values,"
        + f"sum={total}, avg={average}"
        return self.format_output(result)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Text data verification failed")
        count_char = len(data)
        count_word = len(data.split())
        result = f"Processed text: {count_char} characters, {count_word} words"
        return self.format_output(result)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Logo data verification failed")
        if "ERROR" in data:
            message = data.split("ERROR:")[1].strip()
            result = f"[ALERT] ERROR level detected: {message}"
        elif "INFO" in data:
            message = data.split("INFO:")[1].strip()
            result = f"[INFO] INFO level detected: {message}"
        else:
            raise ValueError("Unknown log level")
        return self.format_output(result)

    def format_output(self, result: str) -> str:
        base_output = super().format_output(result)
        return f"{base_output}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION === \n")

    print("Initializing Numeric Processor...")
    num_processor = NumericProcessor()
    try:
        data = [1, 2, 3, 4, 5]
        print(f"Processing data: {data}")
        if num_processor.validate(data):
            print("Validation: Numeric data verified")
        result = num_processor.process(data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Text Processor...")
    text_processor = TextProcessor()
    try:
        data = "Hello Nexus World"
        print(f"Processing data: \"{data}\"")
        if text_processor.validate(data):
            print("Validation: Text data verified")
        result = text_processor.process(data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nInitializing Log Processor...")
    log_processor = LogProcessor()
    try:
        data = "ERROR: Connection timeout"
        print(f"Processing data: \"{data}\"")
        if log_processor.validate(data):
            print("Validation: Log entry verified")
        result = log_processor.process(data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    poli_cases = [
        (num_processor, [2, 2, 2]),
        (text_processor, "hello string"),
        (log_processor, "INFO: System ready")
    ]

    for i, (processor, data) in enumerate(poli_cases, 1):
        try:
            result = processor.process(data)
            final_result = result.replace("Output: ", "")
            print(f"Result {i}: {final_result}")
        except Exception as e:
            print(f"Result {i}: Failed. Error: {e}")


if __name__ == "__main__":
    main()
