from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

DATABASE_URL = "sqlite:///./moisture.db"

engine = create_engine(DATABASE_URL, echo = True)
metadata = MetaData()

plants = Table(
    "plants", metadata,
    Column("id", Integer, primary_key=True),
    Column("species", String),
    Column("moisture_level", Integer),
)

metadata.create_all(engine)

with engine.connect() as conn:
    plant_insert = plants.insert().values(species="Aloe Vera", moisture_level=50)
    conn.execute(plant_insert)
    conn.commit()

