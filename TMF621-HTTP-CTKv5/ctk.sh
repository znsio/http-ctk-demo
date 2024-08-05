#!/bin/bash

specmatic="$DEFAULT_SPECMATIC_PATH"

 docker run -v "./specmatic.yaml:/usr/src/app/specmatic.yaml" znsio/specmatic:2.0.7 test --testBaseURL='http://localhost:8621/tmf-api/troubleTicket/v5'


EXTENSIBLE_SCHEMA=true specmatic test --filter-not-name '/hub,/listener,PATCH,DELETE,-> 202,-> 4,->5' --filter-name '/troubleTicket ->,/troubleTicket/(id:string) ->' --testBaseURL='http://localhost:8621/tmf-api/troubleTicket/v5'

rm -rf ./SEND_ME
mv ./reports/specmatic/html SEND_ME
rm -rf ./reports
