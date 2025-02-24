from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .base_model import (
    FuelResponse,
    ShipCreate,
    ShipResponse,
    TripCreate,
    TripResponse,
    ShipTripCreate,
    ShipTripResponse,
)
from .crud import (
    create_ship,
    create_ship_trip,
    create_trip,
    get_all_fuels,
    get_all_ships,
    get_all_trip_ship,
    get_all_trips,
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


@app.post("/ships", response_model=ShipResponse)
def add_ship(ship: ShipCreate, db: db_dependency):
    return create_ship(ship=ship, db=db)


@app.get("/ships", response_model=List[ShipResponse])
def read_all_ships(db: db_dependency):
    return get_all_ships(db=db)


@app.get("/ships/{ship_id}", response_model=ShipResponse)
def read_ship(ship_id: int, db: db_dependency):
    return get_ship(ship_id=ship_id, db=db)


@app.post("/trips", response_model=TripResponse)
def add_trip(trip: TripCreate, db: db_dependency):
    return create_trip(trip=trip, db=db)


@app.post("/ship-trip", response_model=ShipTripResponse)
def add_ship_trip(ship_trip: ShipTripCreate, db: db_dependency):
    return create_ship_trip(ship_trip=ship_trip, db=db)


@app.get("/trips", response_model=List[TripResponse])
def read_all_trips(db: db_dependency):
    return get_all_trips(db=db)


@app.get("/ship-trip", response_model=List[ShipTripResponse])
def read_all_trip_ship(db: db_dependency):
    return get_all_trip_ship(db=db)


@app.get("/fuels", response_model=List[FuelResponse])
def read_all_fuels(db: db_dependency):
    return get_all_fuels(db=db)
