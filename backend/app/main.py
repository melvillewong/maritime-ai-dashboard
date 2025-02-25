from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .base_model import (
    FuelResponse,
    VesselCreate,
    VesselResponse,
    RouteCreate,
    RouteResponse,
    ShipTripCreate,
    ShipTripResponse,
)
from .crud import (
    create_ship,
    create_ship_trip,
    create_trip,
    delete_all_ships,
    delete_ship,
    get_all_fuels,
    get_all_ships,
    get_all_trip_ship,
    get_all_trips,
    get_fuel,
    get_ship,
)
from .database import engine
from .models import Base
from .dependencies import db_dependency

app = FastAPI()
Base.metadata.create_all(bind=engine)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/vessels", response_model=VesselResponse)
def add_ship(ship: VesselCreate, db: db_dependency):
    return create_ship(ship=ship, db=db)


@app.get("/vessels", response_model=List[VesselResponse])
def read_all_ships(db: db_dependency):
    return get_all_ships(db=db)


@app.get("/vessels/{ship_id}", response_model=VesselResponse)
def read_ship(ship_id: int, db: db_dependency):
    return get_ship(ship_id=ship_id, db=db)


@app.delete("/vessels/{ship_id}")
def remove_ship(ship_id: int, db: db_dependency):
    return delete_ship(ship_id=ship_id, db=db)


@app.delete("/vessels")
def remove_all_ships(db: db_dependency):
    return delete_all_ships(db=db)


@app.post("/routes", response_model=RouteResponse)
def add_trip(trip: RouteCreate, db: db_dependency):
    return create_trip(trip=trip, db=db)


@app.post("/ship-trip", response_model=ShipTripResponse)
def add_ship_trip(ship_trip: ShipTripCreate, db: db_dependency):
    return create_ship_trip(ship_trip=ship_trip, db=db)


@app.get("/routes", response_model=List[RouteResponse])
def read_all_trips(db: db_dependency):
    return get_all_trips(db=db)


@app.get("/ship-trip", response_model=List[ShipTripResponse])
def read_all_trip_ship(db: db_dependency):
    return get_all_trip_ship(db=db)


@app.get("/fuels", response_model=List[FuelResponse])
def read_all_fuels(db: db_dependency):
    return get_all_fuels(db=db)


@app.get("/fuels/{fuel_name}", response_model=FuelResponse)
def read_fuel(fuel_name: str, db: db_dependency):
    return get_fuel(fuel_name=fuel_name, db=db)
