def calc_time_hour(distance: float, speed: float) -> float:
    return distance / speed


# Adjust consumption based on DWT (assuming 50000 DWT is the baseline)
def calc_dwt_adj(dwt: float) -> float:
    return dwt / 50000


# Sector-based fuel consumption adjustment
def calc_sector_multi(sector: str) -> float:
    multi: float = 1
    if sector in ["dt", "ct"]:
        multi = 1.2
    elif sector in ["lng"]:
        multi = 0.8
    return multi


# fuel consumption
def calc_single_consumed(
    distance: float, speed: float, vlfso: float, dwt: float, sector: str
) -> float:
    day_consumed: float = distance / speed
    return day_consumed * vlfso * calc_dwt_adj(dwt) * calc_sector_multi(sector)


def calc_total_consumed(b_consumed: float, l_consumed: float):
    return b_consumed + l_consumed


# emission
def calc_emission(fuel_emission_factor: float, fuel_consumed: float) -> float:
    return fuel_consumed * fuel_emission_factor


# Assume that the weather increases fuel consumption by a margin of 15%
def calc_emission_with_weather(
    fuel_emission_factor: float, fuel_consumed: float
) -> float:
    return (
        calc_emission(
            fuel_emission_factor=fuel_emission_factor, fuel_consumed=fuel_consumed
        )
        * 1.15
    )
