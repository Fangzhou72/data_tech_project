import requests
import os
import json
import time
import sys

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

# imput Twitter Api
def create_url():
    url = "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=created_at%2Clang"
    return url

#Key authorization
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r

#Copy the English text and date of each tweets into tweets.text 
def connect_to_endpoint(url,f):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            if json_response["data"]["lang"] == "en":
            	json_response["data"]["created_at"] = time.strftime("%Y-%m-%d-%H-%M-%S", time.strptime(json_response["data"]["created_at"][:19], "%Y-%m-%dT%H:%M:%S"))
            	new_json_response = json_response["data"]["text"]+"    "+json_response["data"]["created_at"]+"\n"
            	#From: https://stackoverflow.com/questions/214777/how-do-you-convert-yyyy-mm-ddthhmmss-000z-time-format-to-mm-dd-yyyy-time-forma/215313
            	
            	f.write(new_json_response)

            	print(new_json_response)
            	
            	
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    f = open('tweets.txt','w')
    timeout = 0
    while True:
        connect_to_endpoint(url,f)
        timeout += 1



if __name__ == "__main__":
    if len(sys.argv) != 1:
     with open(sys.argv[1], 'r') as fjson:
      contents = fjson.read()
      f = open('tweets.txt','w')
      f.write(contents)
      #From: https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162?fbclid=IwAR3kjvB_uua5NZo1qiSEWSqXYAMgG7a3Y2ynbe14o2Js2JKaps49pA_fTqM
    else:
     main()
    
    
    
    
    
    
    
    
    

