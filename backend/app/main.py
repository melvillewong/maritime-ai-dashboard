from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

from .calculation import (
    calc_fuel_consumed,
    calc_fuel_consumed_with_weather,
    calc_time_hour,
)
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

from .models import Base, Ship, ShipTrip, Trip

app = FastAPI()
Base.metadata.create_all(bind=engine)


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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/ships", response_model=ShipResponse)
def create_ship(ship: ShipCreate, db: db_dependency):
    db_ship = Ship(
        vessel_type=ship.vessel_type,
        fuel_type=ship.fuel_type,
        speed=ship.speed,
    )
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship


@app.get("/ships", response_model=List[ShipResponse])
def get_all_ships(db: db_dependency):
    ships = db.query(Ship).all()

    if len(ships) == 0:
        raise HTTPException(status_code=404, detail="Ship no found")
    return ships


@app.get("/ships/{ship_id}", response_model=ShipResponse)
def get_ship(ship_id: int, db: db_dependency):
    ship = db.query(Ship).filter(Ship.id == ship_id).first()

    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return ship


@app.post("/trips", response_model=TripResponse)
def create_trip(trip: TripCreate, db: db_dependency):
    db_trip = Trip(
        start_port=trip.start_port, end_port=trip.end_port, distance=trip.distance
    )
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


@app.post("/ship-trip", response_model=ShipTripResponse)
def create_ship_trip(ship_trip: ShipTripCreate, db: db_dependency):
    speed: float = db.query(Ship.speed).filter(Ship.id == ship_trip.ship_id).scalar()
    distance: float = (
        db.query(Trip.distance).filter(Trip.id == ship_trip.trip_id).scalar()
    )
    time: float = calc_time_hour(distance=distance, speed=speed)

    fuel_type: str = (
        db.query(Ship.fuel_type).filter(Ship.id == ship_trip.ship_id).scalar()
    )

    fuel_consumed: float = calc_fuel_consumed(time, fuel_type)
    fuel_consumed_weather: float = calc_fuel_consumed_with_weather(time, fuel_type)

    db_ship_trip = ShipTrip(
        ship_id=ship_trip.ship_id,
        trip_id=ship_trip.trip_id,
        time=time,
        fuel_consumed=fuel_consumed,
        fuel_consumed_inc_weather=fuel_consumed_weather,
    )
    db.add(db_ship_trip)
    db.commit()
    db.refresh(db_ship_trip)
    return db_ship_trip


@app.get("/trips", response_model=List[TripResponse])
def get_all_trips(db: db_dependency):
    trips = db.query(Trip).all()

    if len(trips) == 0:
        raise HTTPException(status_code=404, detail="Trip no found")
    return trips


@app.get("/ship-trip", response_model=List[ShipTripResponse])
def get_all_trip_ship(db: db_dependency):
    ship_trip = db.query(ShipTrip).all()

    if len(ship_trip) == 0:
        raise HTTPException(status_code=404, detail="Record no found")
    return ship_trip
