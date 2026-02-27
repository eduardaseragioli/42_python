from abc import ABC, abstractmethod
from typing import Any, List


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

    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for item in data:
            if not isinstance(item, (int, float)):
                return False
        return True
    

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError ("Numeric data verification failed")
        count = len(data)
        total = sum(data)
        if count > 0:
            average = total / count
        else:
            average = 0.0
        result = f"Processed {count} numeric values, sum={total}, avg={average}"
        return self.format_output(result)



class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        print("Validation: Text data verified")
        return True
        

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Text data verification failed")
        count_char = len(data)
        count_word = len(data.split())
        result = f"Processed text: {count_char} characters, {count_word} words"
        return self.format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        print("Validation: Log entry verified")
        return True
            

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Logo data verification failed")
        


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION === \n")

    print("=== Polymorphic Processing Demo ===")


if __name__ == "__main__":
    main()
