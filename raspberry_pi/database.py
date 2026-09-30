from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData


DATABASE_URL = "sqlite:///./moisture.db"

engine = create_engine(DATABASE_URL, echo = True)
metadata = MetaData()

class Plant:
    def __init__(self, species, ideal_moisture_level):
        self.species = species
        self.ideal_moisture_level = ideal_moisture_level


plants = Table(
    "plants", metadata,
    Column("id", Integer, primary_key=True),
    Column("species", String),
    Column("ideal_moisture_level", Integer),
)

readings_001 = Table(
    "readings_001", metadata,
    Column("id", Integer, primary_key=True),
    Column("date", String),
    Column("moisture_level", Integer),
)

readings_002 = Table(
    "readings_002", metadata,
    Column("id", Integer, primary_key=True),
    Column("date", String),
    Column("moisture_level", Integer),
)

metadata.create_all(engine)


with engine.connect() as conn:
    plant_insert = plants.insert().values(species="Aloe Vera", ideal_moisture_level=50)
    conn.execute(plant_insert)
    conn.commit()

