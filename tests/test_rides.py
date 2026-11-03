import os

import pytest

from mobility_stats.rides import (
    average_duration,
    busiest_start_station,
    count_by_rider_type,
    filter_long_rides,
    load_rides,
)


def data_path():
    return os.path.join(os.path.dirname(__file__), "..", "data", "rides.csv")


def test_load_rides_reads_all_rows():
    rides = load_rides(data_path())
    assert len(rides) == 8
    assert rides[0]["ride_id"] == "R001"
    assert rides[0]["duration_min"] == 12.0


def test_load_rides_missing_file():
    with pytest.raises(FileNotFoundError):
        load_rides("does-not-exist.csv")


def test_average_duration():
    rides = load_rides(data_path())
    assert average_duration(rides) == pytest.approx(23.5)


def test_average_duration_empty_list():
    assert average_duration([]) == 0.0


def test_count_by_rider_type():
    rides = load_rides(data_path())
    assert count_by_rider_type(rides) == {"member": 5, "casual": 3}


def test_busiest_start_station():
    rides = load_rides(data_path())
    assert busiest_start_station(rides) == "Central Station"


def test_busiest_start_station_rejects_empty_list():
    with pytest.raises(ValueError, match="must not be empty"):
        busiest_start_station([])


def test_filter_long_rides():
    rides = load_rides(data_path())
    long_rides = filter_long_rides(rides, 30)
    assert [ride["ride_id"] for ride in long_rides] == ["R003", "R005", "R007"]
