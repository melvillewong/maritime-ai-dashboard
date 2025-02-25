from pydantic import BaseModel


class VesselCreate(BaseModel):
    deadweight_mt: float
    fuel_type: str
    ballast_speed_knts: float
    ballast_vlsfo_mt_day: float
    laden_speed_knts: float
    laden_vlsfo_mt_day: float
    sector: str


class VesselResponse(BaseModel):
    id: int
    deadweight_mt: float
    fuel_type: str
    ballast_speed_knts: float
    ballast_vlsfo_mt_day: float
    laden_speed_knts: float
    laden_vlsfo_mt_day: float
    sector: str


class RouteCreate(BaseModel):
    port_1: str
    port_2: str
    distance: float


class RouteResponse(BaseModel):
    id: int
    port_1: str
    port_2: str
    distance: float


class ShipTripCreate(BaseModel):
    vessel_id: int
    route_id: int


class ShipTripResponse(BaseModel):
    vessel_id: int
    route_id: int
    b_fuel_consumed: float
    l_fuel_consumed: float
    return_fuel_consumed: float
    b_emission: float
    l_emission: float
    return_emission: float
    b_emission_inc_weather: float
    l_emission_inc_weather: float
    return_emission_inc_weather: float


class FuelResponse(BaseModel):
    fuel_type: str
    co2_factor: float
    cost: float
