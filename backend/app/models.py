from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class Vessel(Base):
    __tablename__ = "vessels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    deadweight_mt: Mapped[float] = mapped_column(Float, nullable=False)
    fuel_type: Mapped[str] = mapped_column(
        ForeignKey("fuels.fuel_type"), nullable=False
    )
    ballast_speed_knts: Mapped[float] = mapped_column(Float, nullable=False)
    ballast_vlsfo_mt_day: Mapped[float] = mapped_column(Float, nullable=False)
    laden_speed_knts: Mapped[float] = mapped_column(Float, nullable=False)
    laden_vlsfo_mt_day: Mapped[float] = mapped_column(Float, nullable=False)
    sector: Mapped[str] = mapped_column(String, nullable=False)

    routes = relationship("ShipTrip", back_populates="vessel")
    fuel = relationship("Fuel", back_populates="vessels")


class Route(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    port_1: Mapped[str] = mapped_column(String, nullable=False)
    port_2: Mapped[str] = mapped_column(String, nullable=False)
    distance: Mapped[float] = mapped_column(Float, nullable=False)

    vessels = relationship("ShipTrip", back_populates="route")


class ShipTrip(Base):
    __tablename__ = "ship_trips"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vessel_id: Mapped[int] = mapped_column(ForeignKey("vessels.id"), nullable=False)
    route_id: Mapped[int] = mapped_column(ForeignKey("routes.id"), nullable=False)
    b_fuel_consumed: Mapped[float] = mapped_column(Float, nullable=False)
    l_fuel_consumed: Mapped[float] = mapped_column(Float, nullable=False)
    return_fuel_consumed: Mapped[float] = mapped_column(Float, nullable=False)
    b_emission: Mapped[float] = mapped_column(Float, nullable=False)
    l_emission: Mapped[float] = mapped_column(Float, nullable=False)
    return_emission: Mapped[float] = mapped_column(Float, nullable=False)
    b_emission_inc_weather: Mapped[float] = mapped_column(Float, nullable=False)
    l_emission_inc_weather: Mapped[float] = mapped_column(Float, nullable=False)
    return_emission_inc_weather: Mapped[float] = mapped_column(Float, nullable=False)

    vessel = relationship("Vessel", back_populates="routes")
    route = relationship("Route", back_populates="vessels")


class Fuel(Base):
    __tablename__ = "fuels"

    fuel_type: Mapped[str] = mapped_column(String, primary_key=True)
    co2_factor: Mapped[float] = mapped_column(Float, nullable=False)
    cost: Mapped[float] = mapped_column(Float, nullable=True)

    vessels = relationship("Vessel", back_populates="fuel")
