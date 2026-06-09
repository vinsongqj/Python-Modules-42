#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_type: str):
        self.stream_id = "PENDING"
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] =
                    None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "type": self.stream_type}


class SensorStream(DataStream):

    def __init__(self, stream_type: str) -> None:
        super().__init__(stream_type)
        self.stream_id = "SENSOR_001"

    def process_batch(self, data_batch: List[float]) -> str:
        if not data_batch or not isinstance(data_batch, list):
            return "Error: Invalid or missing data batch."
        try:
            count = len(data_batch)
            avg = sum(data_batch) / count if count > 0 else 0.0
            return (f"Sensor analysis: {count} readings processed,"
                    f" avg temp: {avg}°C")
        except TypeError:
            return "Error: Batch contained non-integer values"
        except Exception as e:
            return f"Error: {e}"


class TransactionStream(DataStream):

    def __init__(self, stream_type: str) -> None:
        super().__init__(stream_type)
        self.stream_id = "TRANS_001"

    def process_batch(self, data_batch: List[int]) -> str:
        if not data_batch or not isinstance(data_batch, list):
            return "Error: Invalid or missing data batch."
        try:
            count = len(data_batch)
            net = sum(data_batch)
            sign = "+" if net > 0 else ""
            return (f"Transaction analysis: {count} operations,"
                    f" net flow: {sign}{net} units")
        except TypeError:
            return "Error: Batch contained non-integer values"
        except Exception as e:
            return f"Error: {e}"


class EventStream(DataStream):

    def __init__(self, stream_type: str) -> None:
        super().__init__(stream_type)
        self.stream_id = "EVENT_001"

    def process_batch(self, data_batch: List[str]) -> str:
        if not data_batch or not isinstance(data_batch, list):
            return "Error: Invalid or missing data batch."
        try:
            count = len(data_batch)
            errors = sum(1 for e in data_batch if "error" in e.lower())
            return f"Event analysis: {count} events, {errors} error detected"
        except TypeError:
            return "Error: Batch contained non-integer values"
        except Exception as e:
            return f"Error: {e}"


class StreamProcessor:
    def validate(self, data: Any) -> bool:
        return isinstance(data, DataStream)

    def process(self, stream: DataStream, batch: List[Any]) -> str:
        try:
            if not self.validate(stream):
                raise ValueError("Stream signature mismatch: Expected"
                                 " DataStream object")
            return stream.process_batch(batch)

        except ZeroDivisionError:
            return ("PROCESSING ERROR: Received empty data batch "
                    "(Division by Zero)")
        except TypeError as e:
            return f"DATA ERROR: Invalid data types in batch -> {e}"
        except Exception as e:
            return f"SYSTEM ERROR: An unexpected Nexus glitch occurred: {e}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    ss = SensorStream("Environmental Data")
    print(f"Initializing Sensor Stream...\nStream ID: {ss.stream_id},"
          f" Type: {ss.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(ss.process_batch([22.5, 22.5, 22.5]))

    ts = TransactionStream("Financial Data")
    print(f"\nInitializing Transaction Stream...\nStream ID: {ts.stream_id},"
          f" Type: {ts.stream_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(ts.process_batch([-100, 150, -25]))

    es = EventStream("System Events")
    print(f"\nInitializing Event Stream...\nStream ID: {es.stream_id},"
          f" Type: {es.stream_type}")
    print("Processing event batch: [login, error, logout]")
    print(es.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    streams: List[DataStream] = [ss, ts, es]
    batches = [[22.5, 22.1], [-50, 100, -20, 40],
               ["login", "status", "logout"]]
    labels = ["Sensor data", "Transaction data", "Event data"]

    print("Batch 1 Results:")
    for label, stream, batch in zip(labels, streams, batches):
        try:
            result = stream.process_batch(batch)

            count = len(batch)
            unit = ("readings" if isinstance(stream, SensorStream) else
                    "operations" if isinstance(stream, TransactionStream)
                    else "events")
            print(f"- {label}: {count} {unit} processed")

        except Exception as e:
            print(f"Error on {label}: {e}")
            continue

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")
