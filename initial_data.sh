#! /usr/bin/env bash

# Let the DB start
python /app/initial_data/backend_prestart.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /app/initial_data/initial_data.py