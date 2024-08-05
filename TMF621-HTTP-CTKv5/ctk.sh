#!/bin/bash

specmatic="$DEFAULT_SPECMATIC_PATH"

rm -rf ./SEND_ME

docker run -e EXTENSIBLE_SCHEMA=true -v './SEND_ME:/usr/src/app/reports/specmatic/html:rw' -v "./specmatic.yaml:/usr/src/app/specmatic.yaml" znsio/specmatic:2.0.7 test --filter-not-name '/hub,/listener,PATCH,DELETE,-> 202,-> 4,->5' --filter-name '/troubleTicket ->,/troubleTicket/(id:string) ->' --testBaseURL='http://host.docker.internal:8621/tmf-api/troubleTicket/v5'


# EXTENSIBLE_SCHEMA=true specmatic test --filter-not-name '/hub,/listener,PATCH,DELETE,-> 202,-> 4,->5' --filter-name '/troubleTicket ->,/troubleTicket/(id:string) ->' --testBaseURL='http://localhost:8621/tmf-api/troubleTicket/v5'


# mv ./reports/specmatic/html SEND_ME
# rm -rf ./reports
