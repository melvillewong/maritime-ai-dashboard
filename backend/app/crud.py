from fastapi import HTTPException
from .base_model import (
    VesselCreate,
    RouteCreate,
    ShipTripCreate,
)
from .models import Fuel, Vessel, ShipTrip, Route
from .calculation import (
    calc_emission,
    calc_emission_with_weather,
    calc_single_consumed,
    calc_total_consumed,
)
from .dependencies import db_dependency


def create_ship(ship: VesselCreate, db: db_dependency):
    db_ship = Vessel(
        deadweight_mt=ship.deadweight_mt,
        fuel_type=ship.fuel_type,
        ballast_speed_knts=ship.ballast_speed_knts,
        ballast_vlsfo_mt_day=ship.ballast_vlsfo_mt_day,
        laden_speed_knts=ship.laden_speed_knts,
        laden_vlsfo_mt_day=ship.laden_vlsfo_mt_day,
        sector=ship.sector,
    )
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship


def get_all_ships(db: db_dependency):
    ships = db.query(Vessel).all()

    if len(ships) == 0:
        raise HTTPException(status_code=404, detail="Ship no found")
    return ships


def get_ship(ship_id: int, db: db_dependency):
    ship = db.query(Vessel).filter(Vessel.id == ship_id).first()

    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return ship


def delete_ship(ship_id: int, db: db_dependency):
    ship = db.query(Vessel).filter(Vessel.id == ship_id).first()

    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")

    db.delete(ship)
    db.commit()
    return {"Deletion": "Successful"}


def delete_all_ships(db: db_dependency):
    ship = db.query(Vessel).delete()
    db.commit()

    if ship == 0:
        raise HTTPException(status_code=404, detail="No ships found")

    return {"Deletion": "Successful"}


def create_trip(trip: RouteCreate, db: db_dependency):
    db_trip = Route(port_1=trip.port_1, port_2=trip.port_2, distance=trip.distance)
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


def create_ship_trip(ship_trip: ShipTripCreate, db: db_dependency):
    dwt: float = (
        db.query(Vessel.deadweight_mt).filter(Vessel.id == ship_trip.vessel_id).scalar()
    )
    b_speed: float = (
        db.query(Vessel.ballast_speed_knts)
        .filter(Vessel.id == ship_trip.vessel_id)
        .scalar()
    )
    b_vlsfo: float = (
        db.query(Vessel.ballast_vlsfo_mt_day)
        .filter(Vessel.id == ship_trip.vessel_id)
        .scalar()
    )
    l_speed: float = (
        db.query(Vessel.laden_speed_knts)
        .filter(Vessel.id == ship_trip.vessel_id)
        .scalar()
    )
    l_vlsfo: float = (
        db.query(Vessel.laden_vlsfo_mt_day)
        .filter(Vessel.id == ship_trip.vessel_id)
        .scalar()
    )
    sector: str = (
        db.query(Vessel.sector).filter(Vessel.id == ship_trip.vessel_id).scalar()
    )
    distance: float = (
        db.query(Route.distance).filter(Route.id == ship_trip.route_id).scalar()
    )
    fuel_type: str = (
        db.query(Vessel.fuel_type).filter(Vessel.id == ship_trip.vessel_id).scalar()
    )

    emission_factor: float = (
        db.query(Fuel.co2_factor).filter(Fuel.fuel_type == fuel_type).scalar()
    )

    b_fuel_consumed: float = calc_single_consumed(
        distance, b_speed, b_vlsfo, dwt, sector
    )
    l_fuel_consumed: float = calc_single_consumed(
        distance, l_speed, l_vlsfo, dwt, sector
    )
    return_fuel_consumed: float = calc_total_consumed(b_fuel_consumed, l_fuel_consumed)

    b_emission: float = calc_emission(emission_factor, b_fuel_consumed)
    l_emission: float = calc_emission(emission_factor, b_fuel_consumed)
    return_emission: float = calc_emission(emission_factor, return_fuel_consumed)

    b_emission_weather: float = calc_emission_with_weather(
        emission_factor, b_fuel_consumed
    )
    l_emission_weather: float = calc_emission_with_weather(
        emission_factor, l_fuel_consumed
    )
    return_emission_weather: float = calc_emission_with_weather(
        emission_factor, return_fuel_consumed
    )

    db_ship_trip = ShipTrip(
        vessel_id=ship_trip.vessel_id,
        route_id=ship_trip.route_id,
        b_fuel_consumed=b_fuel_consumed,
        l_fuel_consumed=l_fuel_consumed,
        return_fuel_consumed=return_fuel_consumed,
        b_emission=b_emission,
        l_emission=l_emission,
        return_emission=return_emission,
        b_emission_inc_weather=b_emission_weather,
        l_emission_inc_weather=l_emission_weather,
        return_emission_inc_weather=return_emission_weather,
    )
    db.add(db_ship_trip)
    db.commit()
    db.refresh(db_ship_trip)
    return db_ship_trip


def get_all_trips(db: db_dependency):
    trips = db.query(Route).all()

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
    fuel = db.query(Fuel).filter(Fuel.fuel_type == fuel_name).first()

    if fuel is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return fuel
