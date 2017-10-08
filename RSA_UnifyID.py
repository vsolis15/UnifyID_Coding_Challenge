#import requests
import urllib.request
import json
from math import sqrt
from itertools import count, islice
#from jsonrpc2 import JsonRpc


#credit to https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
# for this prime number function
def is_Prime(n):
    if (n < 2): 
        return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not (n%number):
            return False
    return True

def main():
    url = "https://api.random.org/json-rpc/1/invoke"
    headers = {'content-type': 'application/json'}

    quest = urllib.request.Request(url)

    quest.add_header('Content-Type', 'application/json; charset=utf-8')

    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": { 
            "apiKey": "23b26322-8f4b-45e1-9e7c-51a800292396",
            "n": 100,
            "min": 1000,
            "max": 10000,
            "replacement": False
        },
        "id": 0,
    }

    jsondata = json.dumps(payload)
    jsondataasbytes = jsondata.encode('utf-8')
    quest.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(quest, jsondataasbytes)
    string = response.read().decode('utf-8')

    response = json.loads(string)

    # Example echo method
    
    #response = requests.post(
    #    url, data=json.dumps(payload), headers=headers).json()

    #print(response.)
    #for key in response:
    #    print(key)

    poss_primes = response["result"]["random"]["data"]

    p = 0
    q = 0
    i = 0

    while(((p == 0) or (q == 0)) and i < len(poss_primes)):
        num = int(poss_primes[i])
        prime = False
        prime = is_Prime(num)
        if (prime):
            if (p == 0):
                p = num
            elif (q == 0):
                q = num
        i += 1

    #assert p != 0
    #assert q != 0
    n = p * q

    if ((p == 0) or (q == 0)):
        print("Not enough primes run again to find more")
    else:
        eulers = (p - 1) * (q - 1)
        public_key = 19

        private_key = ((1 / 19) % eulers)

        print("Your prime number p is " + str(p) + " Your prime number q is " + str(q))
        print("Public Key is 19")
        print("Private Key is " + str(private_key))

    # assert response["result"] == "echome!"
    # assert response["jsonrpc"]
    # assert response["id"] == 0

if __name__ == "__main__":
    main()