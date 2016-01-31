import json, time
import requests
import datetime
import os

if os.path.exists('config.txt'):
    access_token=''
    config_file = open('config.txt','r')
    for line in config_file.readlines():
        if 'access_token' in line:
            access_token = line.split('=')[1]
            #print(access_token)
        else:
            print("Error in config file. Define access_token first.")
            exit("Exiting")
    config_file.close()
else:
    print("No config file present. Please create a config.txt as such: access_token=xxxx")
    exit("Exiting...no config file.")

response = requests.get('https://api.instagram.com/v1/users/self/feed?access_token='+str(access_token)+'&count=40')

json_data = json.loads(response.text)
json_length = len(json_data['data'])
print("The full json length is: " + str(json_length))

var = 1
while var == 1:
    print('Time of run: ' + str(datetime.datetime.now()))
    print('Started liking...hold tight!')
    for itr in range(0, json_length, 1):
        #image_url = (json_data['data'][itr]['images']['standard_resolution']['url'])
        image_id = (json_data['data'][itr]['id']).split('_')[0]
        #print(image_url)

        #print(image_id)
        like_url = "https://api.instagram.com/v1/media/"+image_id+"/likes?access_token="+str(access_token)
        r = requests.post(like_url)
        print(itr)
        print(r.text)
        time.sleep(2)

    print('Sleeping for 1 hour. I\'ll be back. \nBye bye')
    time.sleep(3660)