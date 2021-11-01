import pandas as pd
import pathlib

from sqlalchemy.orm import Session

from app.models.location import Location


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    data_path = pathlib.Path().resolve().parent.joinpath("app/data")
    location_examples_file = data_path.joinpath("location_examples.csv")
    locations_df = pd.read_csv(location_examples_file)
    locations_list = []
    for index, location in locations_df.iterrows():
        new_location = Location(location_name=location["city_ascii"], latitude=location["lat"],
                                longitude=location["lng"])
        locations_list.append(new_location)
    db.add_all(locations_list)
    db.commit()
