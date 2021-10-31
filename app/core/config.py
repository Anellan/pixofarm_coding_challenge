from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator, Field


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    WEATHERBIT_API_KEY: str = Field(..., env="WEATHERBIT_API_KEY")
    WEATHERBIT_BASE_URL: str = "http://api.weatherbit.io/v2.0"
    HISTORY_LAT_LNG_ENDPOINT: str = "/history/daily"
    ENDPOINT_PARAMS: str = "?lat={lat}&lon={lon}&start_date={start_date}&end_date={end_date}&key={key}"


settings = Settings()
