from pysislab import get_sensors, SensorTail

def test_get_sensors():
    sensors = get_sensors()
    assert len(sensors) > 0
    assert sensors[0].id == 1
    assert sensors[0].secondary_id == "AM.R02C9"
    assert sensors[0].type == "Raspberry Shake 4D"

def test_sensor_tail():
    sensor_tail = SensorTail(22)

    it = sensor_tail.__iter__()

    assert it is sensor_tail

    datagram = sensor_tail.__next__()

    assert datagram.channel in ["EHZ", "ENN", "ENZ", "ENE"]
    assert datagram.timestamp > 0
    assert len(datagram.data) >= 25
