# Instructions

## Pre-requisites
- Ensure that you have Docker Desktop running


## Run the Dockerized RI 
```shell
cd TMF621-HTTP-RIv5
./ri.sh
```

## Run the Dockerized CTK
```shell
cd TMF621-HTTP-CTKv5
./ctk.sh
```

```shell
open ./TMF621-HTTP-CTKv5/SEND_ME/index.html
```
- Check the sample-cypress-CTK-report dir to see how the cypress-based report looks... try to expand the test sections.. it has no request-response payloads.

#### Legacy RI
```shell
cd TMF621-HTTP-RIv5
docker compose up --build
```