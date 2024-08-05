# Instructions

## Pre-requisites

- Build the Specmatic docker image locally
  - Pull latest from the Specmatic repo
  - checkout `html-report` branch
  - run `./gradlew assemble` (some tests related to the report are failing)
  - run `./build-local-docker-image.sh`
- Clone https://github.com/znsio/http-ctk-demo/
- Ensure that you have Docker Desktop running

## Run Denis' RI

- cd into the `http-ctk-demo` repo that you checked out
- cd into `TMF621-HTTP-RIv5` (contains the same docker compose file as TMF621e but with the bridge removed)
- run docker compose up --build

## Run the tests

- In a new tab, cd into `TMF621-HTTP-CTKv5`
- run `./ctk.sh`
- View the report
  - run open ./SEND_ME/index.html
  - Check the sample-cypress-CTK-report dir to see how the cypress-based report looks... try to expand the test sections.. it has no request-response payloads.

## Run the Dockerized RI (Specmatic stub-based setup)

- cd into `TMF621-HTTP-RIv5`
- run `./ri.sh`
