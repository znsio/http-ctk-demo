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
```shell
cd TMF621-HTTP-RIv5
docker compose up --build
```

## Run the tests
```shell
cd TMF621-HTTP-CTKv5
./ctk.sh
```

```shell
open ./TMF621-HTTP-CTKv5/SEND_ME/index.html
```
- Check the sample-cypress-CTK-report dir to see how the cypress-based report looks... try to expand the test sections.. it has no request-response payloads.

## Run the Dockerized RI (Specmatic stub-based setup)
```shell
cd TMF621-HTTP-RIv5
./ri.sh
```