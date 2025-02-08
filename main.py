from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated, List
from database import engine, SessionLocal
from sqlalchemy.orm import Session

import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class ShipCreate(BaseModel):
    vessel_type: str
    fuel_type: str
    distance: float


class ShipResponse(BaseModel):
    id: int
    vessel_type: str
    fuel_type: str
    distance: float

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/ships", response_model=ShipResponse)
def create_ship(ship: ShipCreate, db: db_dependency):
    db_ship = models.Ship(
        vessel_type=ship.vessel_type, fuel_type=ship.fuel_type, distance=ship.distance
    )
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship


@app.get("/ships", response_model=List[ShipResponse])
def get_all_ships(db: db_dependency):
    ships = db.query(models.Ship).all()
    return ships


@app.get("/ships/{ship_id}", response_model=ShipResponse)
def get_ship(ship_id: int, db: db_dependency):
    ship = db.query(models.Ship).filter(models.Ship.id == ship_id).first()

    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return ship
