import argparse

from rich.console import Console
from rich.table import Table

from . import get_sensors, SensorTail


def print_sensors():
    sensors = get_sensors()

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Raspberry Shake Ref.")
    table.add_column("Type")
    table.add_column("Latitude")
    table.add_column("Longitude")
    table.add_column("Online")
    
    for sensor in sensors:
        table.add_row(
            str(sensor.id),
            sensor.secondary_id,
            sensor.type,
            str(sensor.publicLocation and sensor.publicLocation[0]),
            str(sensor.publicLocation and sensor.publicLocation[1]),
            str(sensor.online),
        )

    console.print(table)

def print_sensors_csv():
    sensors = get_sensors()

    for sensor in sensors:
        print(
            sensor.id,
            sensor.secondary_id,
            sensor.type,
            sensor.publicLocation and sensor.publicLocation[0],
            sensor.publicLocation and sensor.publicLocation[1],
            sensor.online,
            sep=","
        )

def tail(sensor_id: int):
    sensor_tail = SensorTail(sensor_id)

    for datagram in sensor_tail:
        print(datagram.channel, datagram.timestamp, *datagram, sep=",")


def main():
    parser = argparse.ArgumentParser(description='CLI for fetching data from the CRISiSLab seismometer network')
    parser.add_argument('--list', action='store_true', help='List all nodes in the network')
    parser.add_argument('--tail', type=int, help='Follow live data from node')
    parser.add_argument('--csv', action='store_true', help='Output data in CSV format')
    args = parser.parse_args()

    if not args.list and not args.tail:
        parser.print_help()

    if args.list:
        if args.csv:
            print_sensors_csv()
        else:
            print_sensors()
    elif args.tail:
        tail(args.tail)