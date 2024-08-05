#!/bin/bash

docker compose -f ri-compose.yml pull
docker compose -f ri-compose.yml down
docker compose -f ri-compose.yml up --build
