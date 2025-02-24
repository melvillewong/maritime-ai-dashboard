from fastapi import HTTPException
from .base_model import (
    ShipCreate,
    TripCreate,
    ShipTripCreate,
)
from .models import Fuel, Ship, ShipTrip, Trip
from .calculation import (
    calc_fuel_consumed,
    calc_fuel_consumed_with_weather,
    calc_time_hour,
)
from .dependencies import db_dependency


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


def get_all_ships(db: db_dependency):
    ships = db.query(Ship).all()

    if len(ships) == 0:
        raise HTTPException(status_code=404, detail="Ship no found")
    return ships


def get_ship(ship_id: int, db: db_dependency):
    ship = db.query(Ship).filter(Ship.id == ship_id).first()

    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return ship


def create_trip(trip: TripCreate, db: db_dependency):
    db_trip = Trip(
        start_port=trip.start_port, end_port=trip.end_port, distance=trip.distance
    )
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


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


def get_all_trips(db: db_dependency):
    trips = db.query(Trip).all()

    if len(trips) == 0:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trips


def get_all_trip_ship(db: db_dependency):
    ship_trip = db.query(ShipTrip).all()

    if len(ship_trip) == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return ship_trip


def get_all_fuels(db: db_dependency):
    fuels = db.query(Fuel).all()

    if len(fuels) == 0:
        raise HTTPException(status_code=404, detail="fuel not found")
    return fuels


def get_fuel(fuel_name: str, db: db_dependency):
    fuel = db.query(Fuel).filter(Fuel.name == fuel_name).first()

    if fuel is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return fuel
