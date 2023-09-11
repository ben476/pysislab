import requests
from typeguard import typechecked
from .models import Sensor
from typing import Any, List

API_URL = "https://shakenet-manager.viggers.workers.dev/api/v0/sensors"

@typechecked
def get_sensors(api_url: str = API_URL) -> List[Sensor]:
    """Get a list of sensors from the ShakeNet API.

    Parameters
    ----------
    api_url : str
        The URL of the ShakeNet API endpoint.

    Returns
    -------
    list
        A list of sensors.
    """
    response = requests.get(api_url)
    response.raise_for_status()

    json: dict[str, dict[Any, Any]] = response.json()["sensors"]

    sensors = [Sensor(**sensor) for sensor in json.values()]

    return sensors