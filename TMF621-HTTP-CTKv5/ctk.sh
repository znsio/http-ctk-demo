#!/bin/bash

rm -rf ./SEND_ME

docker run -e MAX_TEST_REQUEST_COMBINATIONS=5 -e EXTENSIBLE_SCHEMA=true -v './SEND_ME:/usr/src/app/build/reports/specmatic/html:rw' -v "./specmatic.yaml:/usr/src/app/specmatic.yaml" znsio/specmatic:2.0.17 test --filter-not-name '/hub,/listener,PATCH,-> 401,-> 403,/troubleTicket -> 404,DELETE,-> 405,POST /troubleTicket -> 202,-> 5' --filter-name '/troubleTicket ->,/troubleTicket/(id:string) ->' --testBaseURL='http://host.docker.internal:8621/tmf-api/troubleTicket/v5'

