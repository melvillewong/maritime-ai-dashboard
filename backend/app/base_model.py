from pydantic import BaseModel


class ShipCreate(BaseModel):
    vessel_type: str
    fuel_type: str
    speed: float


class ShipResponse(BaseModel):
    id: int
    vessel_type: str
    fuel_type: str
    speed: float


class TripCreate(BaseModel):
    start_port: str
    end_port: str
    distance: float


class TripResponse(BaseModel):
    id: int
    start_port: str
    end_port: str
    distance: float


class ShipTripCreate(BaseModel):
    ship_id: int
    trip_id: int


class ShipTripResponse(BaseModel):
    ship_id: int
    trip_id: int
    time: float
    fuel_consumed: float
    fuel_consumed_inc_weather: float


class FuelResponse(BaseModel):
    name: str
    co2_factor: float
    cost: float
