import requests
import datetime

host = 'TP-FH4F-FW-01'

current_time = datetime.datetime.today().strftime('%Y_%b_%d') # This is to add to the naming of the file

api_token = 'cqQkstGHxq4kb1wNhpbz1b11wh0byp'

api_url = 'https://10.22.65.1/api/v2/monitor/system/config/backup?scope=global&access_token=' + api_token

requests.packages.urllib3.disable_warnings() # Close https CA warning

data = requests.get(api_url, verify=False) # disable SSL https url verification

with open('C:/Users/user/Desktop/backups/' + str(host) + '_' + str(current_time) + '.conf', 'wb') as f:
    for line in data:
        f.write(line)

#print(data.status_code) output status code
#print(data.text) Output config

