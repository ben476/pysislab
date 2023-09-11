from typing import Iterator, Optional
from typeguard import typechecked
from websocket import WebSocket 
import msgpack

@typechecked
class Datagram:
    """Class to represent a single datagram from a sensor.

    Parameters
    ----------
    channel : str
        The seismic channel the datagram is from.
    timestamp : float
        The time of the first sample in the datagram in seconds since the epoch.
    data : list[int]
        The samples in the datagram.
    """

    channel: str
    timestamp: float
    data: list[int]

    def __init__(self, channel: str, timestamp: float, data: list[int]):
        self.channel = channel
        self.timestamp = timestamp
        self.data = data

    def __iter__(self) -> Iterator[int]:
        return iter(self.data)
    
    def __str__(self) -> str:
        return f"{self.channel} {self.timestamp} {self.data}"

@typechecked
class SensorTail(Iterator[Datagram]):
    """Class to watch live data from a sensor.

    Parameters
    ----------
    sensor_id : int
        The ID of the sensor to watch.
    api_url : str, optional
        The URL of the Shakemap API endpoint.
    """
    sensor_id: int
    api_url: str
    ws: WebSocket = WebSocket()

    def __init__(self, sensor_id: int, api_url: Optional[str] = None):
        self.sensor_id = sensor_id
        self.api_url = api_url or f"wss://crisislab-data.massey.ac.nz/consume/{self.sensor_id}/live"

    def __iter__(self) -> Iterator[Datagram]:
        self.ws.connect(self.api_url) # type: ignore
        return self

    def __next__(self) -> Datagram:
        data = self.ws.recv()
        parsed = msgpack.loads(data)

        if parsed["type"] == "datagram":
            # TODO: handle multiple datagrams in one message
            channel, timestamp, *data = parsed["data"][0]

            return Datagram(channel, timestamp, data)
        
        if parsed["type"] == "sensor-meta":
            self.sensor_meta = parsed["data"]
            if self.sensor_meta["online"] != True:
                raise Exception(f"Sensor #{self.sensor_id} seems to be offline.")
        
        return self.__next__()

    def __del__(self):
        self.ws.close() # type: ignore
