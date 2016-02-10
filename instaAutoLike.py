import json
import time
import requests
import datetime
import os

print('\t\t####################################')
print('\t\t####################################')
print('\t\t####### Insta Auto Like Bot  #######')
print('\t\t####################################')
print('\t\t# Developed by Abhishek Srivastava #')
print('\t\t####################################')
print('\t\t####################################')

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
    print("No config file present. Please create a config.txt as such: access_token=xxxx\nPlease open the readme file to know more")
    exit("Exiting...no config file.")

response = requests.get('https://api.instagram.com/v1/users/self/feed?access_token='+str(access_token)+'&count=40')

json_data = json.loads(response.text)
json_length = len(json_data['data'])
print("The full json length is: " + str(json_length))

var = 1
while var == 1:
    print('Time of run: ' + str(time.strftime("%Y-%m-%d %H:%M")))
    print('Started liking...hold tight!')
    err_count = 0
    for itr in range(0, json_length, 1):

        #image_url = (json_data['data'][itr]['images']['standard_resolution']['url'])
        image_id = (json_data['data'][itr]['id']).split('_')[0]
        #print(image_url)

        #print(image_id)
        like_url = "https://api.instagram.com/v1/media/"+image_id+"/likes?access_token="+str(access_token)
        r = requests.post(like_url)
        print('Liking image # %s' % str(itr+1))
        #print(r.text)
        json_resp = json.loads(r.text)
        #print str(json_resp['meta']['code'])
        if json_resp['meta']['code'] == 200:
            print 'Like successful :)'
        elif json_resp['meta']['error_type'] == "OAuthRateLimitException":
            print 'Like failed. Error: %s' % json_resp['meta']['error_message']
            err_count += 1
            if err_count > 2:
                print "\nToo many requests made. Sleeping for one hour. \nDon't worry, just keep the window open. I'll retry after an hour"
                time.sleep(3660)
        else:
            print 'Like failed. Error: %s' % json_resp['meta']['error_message']
        time.sleep(2)

    print('Sleeping for 1 hour. I\'ll be back. \nDon\'t close this window to keep the bot running. Bye bye')
    time.sleep(3660)
