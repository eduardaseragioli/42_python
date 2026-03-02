from abc import ABC, abstractmethod
from typing import Any, List, Dict,  Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id}


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
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
        return f"Transaction analysis: {self.total_operations} operations, net flow: +{self.net_flow} units"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered_data = []
        for trans in data_batch:
            if isinstance(trans, str):
                trans_item = trans.split(":")
                if trans_item[0] == criteria:
                    filtered_data.append(trans)
        return filtered_data

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
        self.total_events = 0
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_events = 0
        self.error_count = 0
        for item in data_batch:
            if isinstance(item, str):
                self.total_events += 1
                if item == "error":
                    self.error_count += 1
        return f"Event analysis: {self.total_events} events, {self.error_count} error detected"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered = []
        for event in data_batch:
            if event == criteria:
                filtered.append(event)
        return filtered

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
        self.readings_processed = 0
        self.avg_temp = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
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

        return f"Sensor analysis: {self.readings_processed} readings processed, avg temp: {self.avg_temp}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered = []
        for reading in data_batch:
            if isinstance(reading, str):
                sensor_type = reading.split(":")[0]
                if sensor_type == criteria:
                    filtered.append(reading)
        return filtered

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
            if isinstance(stream, SensorStream):
                result = stream.process_batch(batches["sensor"])
                print(f"- Sensor data: {stream.readings_processed} readings processed")
            elif isinstance(stream, TransactionStream):
                result = stream.process_batch(batches["transaction"])
                print(f"- Transaction data: {stream.total_operations} operations processed")
            elif isinstance(stream, EventStream):
                result = stream.process_batch(batches["event"])
                print(f"- Event data: {stream.total_events} events processed") 
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]=None) -> List[Any]:
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
    
    # Criar dados misturados para filtrar
    mixed_data = [
        "temp:-5", "temp:45", "buy:1000", "error", "pressure:900",
        "humidity:80", "sell:50", "login"
    ]
    
    # Contar alertas críticos de sensor (temperaturas extremas)
    critical_sensors = 0
    for data in mixed_data:
        if isinstance(data, str) and "temp:" in data:
            temp_val = float(data.split(":")[1])
            if temp_val < 0 or temp_val > 40:
                critical_sensors += 1
    
    # Contar transações grandes
    large_trans = 0
    for data in mixed_data:
        if isinstance(data, str) and ("buy:" in data or "sell:" in data):
            amount = int(data.split(":")[1])
            if amount >= 500:
                large_trans += 1
    
    print(f"Filtered results: {critical_sensors} critical sensor alerts, {large_trans} large transaction")
    
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
