# Perform manual alembic migrations

### Create migration script
docker-compose run app alembic revision --autogenerate -m "Init"

### Make migration
docker-compose run app alembic upgrade head

### Downgrade
docker-compose run app alembic downgrade -1

### Init Db with alembic migration
docker-compose run app bash -c "chmod +x ./initial_data.sh && ./initial_data.sh"

### Get weather reports
docker-compose run app python initial_data/get_weather_reports.py