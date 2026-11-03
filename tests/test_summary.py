from mobility_stats.summary import build_summary, format_summary


def test_build_summary():
    rides = [
        {
            "ride_id": "R1",
            "start_station": "A",
            "end_station": "B",
            "duration_min": 10.0,
            "rider_type": "member",
        },
        {
            "ride_id": "R2",
            "start_station": "A",
            "end_station": "C",
            "duration_min": 20.0,
            "rider_type": "casual",
        },
    ]
    summary = build_summary(rides)
    assert summary["ride_count"] == 2
    assert summary["average_duration"] == 15.0
    assert summary["busiest_start_station"] == "A"


def test_format_summary():
    summary = {
        "ride_count": 2,
        "average_duration": 15.0,
        "rider_types": {"member": 1, "casual": 1},
        "busiest_start_station": "A",
    }
    text = format_summary(summary)
    assert "Rides: 2" in text
    assert "Average duration: 15.0 min" in text
    assert "Busiest start: A" in text
