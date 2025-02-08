from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vessel_type: Mapped[str] = mapped_column(String, nullable=False)
    fuel_type: Mapped[str] = mapped_column(String, nullable=False)
    distance: Mapped[float] = mapped_column(Float, nullable=False)
