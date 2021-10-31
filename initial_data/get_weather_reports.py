import pandas as pd
import requests
# import aiohttp
# import asyncio

from app.core.config import settings
from sqlalchemy.orm import Session
from app.models.location import Location
from app.models.timeseries import TimeSeries
from datetime import datetime
import logging

from init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_locations(db: Session) -> None:
    # Tables should be created with Alembic migrations
    return db.query(Location).all()


def query_weatherbit(db: Session):
    timeseries_objects = []
    date_list = pd.date_range("2020-12-01", "2021-02-01", periods=10).to_list()
    location_list = get_locations(db)
    for location in location_list:
        start_date_index = 0
        end_date_index = start_date_index + 1
        while end_date_index < len(date_list):
            start_date = date_list[start_date_index].to_pydatetime().strftime("%Y-%m-%d")
            end_date = date_list[end_date_index].to_pydatetime().strftime("%Y-%m-%d")
            start_date_index += 1
            end_date_index += 1
            endpoint_params = settings.ENDPOINT_PARAMS.format(lat=location.latitude, lon=location.longitude,
                                                              start_date=start_date,
                                                              end_date=end_date, key=settings.WEATHERBIT_API_KEY)
            request_url = f'{settings.WEATHERBIT_BASE_URL}{settings.HISTORY_LAT_LNG_ENDPOINT}{endpoint_params}'
            r = requests.get(request_url).json()
            for data in r["data"]:
                ts = data["ts"]
                min_temp = data["min_temp"]
                max_temp = data["max_temp"]
                mean_temp = round((max_temp + min_temp) / 2, 2)
                timeseries = TimeSeries(ts, location.id, min_temp, max_temp, mean_temp)
                timeseries_objects.append((timeseries))
    db.add_all(timeseries_objects)
    db.commit()


def init() -> None:
    db = SessionLocal()
    query_weatherbit(db)


def main() -> None:
    logger.info("Querying date")
    init()
    logger.info("Data inserted")


if __name__ == "__main__":
    main()


# async def get_weather_report(session, url):
#     async with session.get(url) as resp:
#         return await resp.json()
#
#
# # date_list = pd.date_range("2020-12-01", "2021-02-01", periods=10).to_list()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         date_list = pd.date_range("2020-12-01", "2021-12-03", periods=2).to_list()
#
#         start_date_index = 0
#         end_date_index = start_date_index + 1
#
#         while end_date_index < len(date_list):
#             start_date = date_list[start_date_index].to_pydatetime().strftime("%Y-%m-%d")
#             end_date = date_list[end_date_index].to_pydatetime().strftime("%Y-%m-%d")
#             start_date_index += 1
#             end_date_index += 1

# endpoint_params = settings.ENDPOINT_PARAMS.format(lat="35.6897", lon="139.6922", start_date="2020-11-01",
#                                                   end_date="2020-11-08", key=settings.WEATHERBIT_API_KEY)
# request_url = f'{settings.WEATHERBIT_BASE_URL}{settings.HISTORY_LAT_LNG_ENDPOINT}{endpoint_params}'
# r = requests.get(request_url)
# print(r.text)
