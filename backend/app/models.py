from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vessel_type: Mapped[str] = mapped_column(String, nullable=False)
    fuel_type: Mapped[str] = mapped_column(String, nullable=False)
    speed: Mapped[float] = mapped_column(Float, nullable=False)

    trips = relationship("ShipTrip", back_populates="ship")


class Trip(Base):
    __tablename__ = "trips"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_port: Mapped[str] = mapped_column(String, nullable=False)
    end_port: Mapped[str] = mapped_column(String, nullable=False)
    distance: Mapped[float] = mapped_column(Integer, nullable=False)

    ships = relationship("ShipTrip", back_populates="trip")


class ShipTrip(Base):
    __tablename__ = "ship_trips"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ship_id: Mapped[int] = mapped_column(ForeignKey("ships.id"), nullable=False)
    trip_id: Mapped[int] = mapped_column(ForeignKey("trips.id"), nullable=False)
    time: Mapped[float] = mapped_column(Float, nullable=False)
    fuel_consumed: Mapped[float] = mapped_column(Float, nullable=False)
    fuel_consumed_inc_weather: Mapped[float] = mapped_column(Float, nullable=False)

    ship = relationship("Ship", back_populates="trips")
    trip = relationship("Trip", back_populates="ships")
