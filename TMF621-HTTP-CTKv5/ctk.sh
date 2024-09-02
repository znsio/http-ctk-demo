#!/bin/bash

rm -rf ./SEND_ME

source ../env/bin/activate

python conformance_filter.py

FILTER_NAME=$(python conformance_filter.py ./conformance.yaml ../specifications/TMF621/TMF621-Trouble_Ticket-v5.0.0.oas.fixed.yaml)

echo "FILTER NAME"
echo $FILTER_NAME
echo =========

docker run -e MAX_TEST_REQUEST_COMBINATIONS=5 -e EXTENSIBLE_SCHEMA=true -v './SEND_ME:/usr/src/app/build/reports/specmatic/html:rw' -v "./specmatic.yaml:/usr/src/app/specmatic.yaml" znsio/specmatic:2.0.17 test --filter-name "$FILTER_NAME" --testBaseURL='http://host.docker.internal:8621/tmf-api/troubleTicket/v5'
