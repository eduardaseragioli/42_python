from abc import ABC, abstractmethod
from typing import Any, List, Dict,  Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id}


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "transaction"
        self.total_operations = 0
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total_operations = 0
            self.net_flow = 0
            for item in data_batch:
                if isinstance(item, str):
                    trans_item = item.split(":")
                    if trans_item[0] == "buy":
                        self.net_flow += int(trans_item[1])
                    elif trans_item[0] == "sell":
                        self.net_flow -= int(trans_item[1])
                    self.total_operations += 1
            sign = '+' if self.net_flow >= 0 else ''
            return (f"Transaction analysis: {self.total_operations} "
                    f"operations, net flow: {sign}{self.net_flow} units")
        except (ValueError, IndexError) as e:
            return f"Processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch

            filtered_data = [
                trans for trans in data_batch
                if isinstance(trans, str) and trans.split(":")[0] == criteria]

            return filtered_data
        except (ValueError, IndexError) as e:
            print(f"Processing error: {e}")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        status = {
            "id": self.stream_id,
            "total_operations": self.total_operations,
            "net_flow": self.net_flow
        }
        return status


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "event"
        self.total_events = 0
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total_events = 0
            self.error_count = 0
            for item in data_batch:
                if isinstance(item, str):
                    self.total_events += 1
                    if item == "error":
                        self.error_count += 1
            error_text = "error" if self.error_count == 1 else "errors"
            return (f"Event analysis: {self.total_events} events, "
                    f"{self.error_count} {error_text} detected")
        except (ValueError, IndexError) as e:
            return f"Processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            filtered = []
            for event in data_batch:
                if event == criteria:
                    filtered.append(event)
            return filtered
        except (ValueError, IndexError) as e:
            print(f"Processing error: {e}")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        status = {
            "id": self.stream_id,
            "total_events": self.total_events,
            "error_count": self.error_count
        }
        return status


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "sensor"
        self.readings_processed = 0
        self.avg_temp = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.readings_processed = 0
            total_temp = 0.0
            temp_count = 0

            for item in data_batch:
                if isinstance(item, str):
                    self.readings_processed += 1
                    sensor_data = item.split(":")

                    if sensor_data[0] == "temp":
                        temp_value = float(sensor_data[1])
                        total_temp += temp_value
                        temp_count += 1

            if temp_count > 0:
                self.avg_temp = total_temp / temp_count
            else:
                self.avg_temp = 0.0

            return (f"Sensor analysis: {self.readings_processed} "
                    f"readings processed, avg temp: {self.avg_temp}°C")
        except (ValueError, IndexError) as e:
            return f"Processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                return data_batch

            filtered = []
            for reading in data_batch:
                if isinstance(reading, str):
                    sensor_type = reading.split(":")[0]
                    if sensor_type == criteria:
                        filtered.append(reading)
            return filtered
        except (ValueError, IndexError) as e:
            print(f"Processing error: {e}")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        status = {
            "id": self.stream_id,
            "readings_processed": self.readings_processed,
            "avg_temp": self.avg_temp
        }
        return status


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")

        for stream in self.streams:
            batch = batches.get(stream.stream_type)
            stream.process_batch(batch)
            
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stream.readings_processed} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {stream.total_operations} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stream.total_events} events processed")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        final_res = []
        for stream in self.streams:
            stream_alert = stream.filter_data(data_batch, criteria)
            final_res.extend(stream_alert)
        return final_res


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    temp = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {temp}")
    print(sensor.process_batch(temp))

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    transaction_list = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_list}")
    print(transaction.process_batch(transaction_list))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_process = ["login", "error", "logout"]
    print(f"Processing event batch: {event_process}")
    print(event.process_batch(event_process))

    all_poli = StreamProcessor()
    all_poli.add_stream(sensor)
    all_poli.add_stream(transaction)
    all_poli.add_stream(event)

    batches = {
        "sensor": ["temp:20.0", "pressure:1012"],
        "transaction": ["buy:50", "sell:25", "buy:100", "sell:75"],
        "event": ["login", "logout", "error"]
    }

    all_poli.process_all(batches)

    print("\nStream filtering active: High-priority data only")

    mixed_data = [
        "temp:-5", "temp:45", "buy:1000", "error", "pressure:900",
        "humidity:80", "sell:50", "login"
    ]

    critical_sensor_count = 0

    for item in mixed_data:
        if isinstance(item, str) and "temp:" in item:
            parts = item.split(":")
            temp = float(parts[1])
            if temp < 0 or temp > 40:
                critical_sensor_count += 1

    large_transaction_count = 0

    for item in mixed_data:
        if isinstance(item, str) and ("buy:" in item or "sell:" in item):
            parts = item.split(":")
            valor = int(parts[1])
            if valor >= 500:
                large_transaction_count += 1

    print(
        f"Filtered results: {critical_sensor_count} critical sensor alerts, "
        f"{large_transaction_count} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
