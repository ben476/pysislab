# Pysislab - CRISiSLab Seismometer Network Client

## Description

This is a client for [CRISiSLab's Seismometer Network](https://shakemap.crisislab.org.nz/) API using WebSockets and MessagePack.

## Installation

```bash
$ pip install pysislab
```

## Usage

To list all stations (optionally in CSV format)

```bash
$ pysislab --list --csv
```

To watch live data in real time for a particular seismometer

```bash
$ pysislab --tail <seismometer id>
```

Or the equivalent in Python

```python
from pysislab import get_sensors

for sensor in get_sensors():
    print(
        sensor.id,
        sensor.secondary_id,
        sensor.type,
        sensor.publicLocation,
        sensor.online,
    )
```

```python
from pysislab import SensorTail

for datagram in SensorTail(22):
    print(datagram.channel, datagram.timestamp, datagram.data)
```

For more examples, see the [CLI implementation](pysislab/cli.py).

See the [models file](pysislab/models.py) for the full list of attributes available on each class.
