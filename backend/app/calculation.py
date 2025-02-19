from typing import List

# CO2 per fuel type (per tonne of fuel)
fuel_co2_emission: dict[str, float] = {"diesel": 3.114, "lng": 2.75, "hydrogen": 0}

# Vessel type
vessel_type: List[str] = ["container ship", "bulk carrier", "tanker"]


def calc_time_hour(distance: float, speed: float) -> float:
    return distance / speed


def calc_fuel_consumed(time: float, fuel_type: str) -> float:
    return time * fuel_co2_emission[fuel_type]


# Assume that the weather increases fuel consumption by a margin of 15%
def calc_fuel_consumed_with_weather(time: float, fuel_type: str) -> float:
    return calc_fuel_consumed(time=time, fuel_type=fuel_type) * 1.15
