# pixofarm_coding_challenge

### Alembic migrations commands
 - docker-compose build
 - docker-compose run app alembic revision --autogenerate -m "Init"
 - docker-compose run app alembic upgrade head
 - docker-compose run app alembic downgrade -1