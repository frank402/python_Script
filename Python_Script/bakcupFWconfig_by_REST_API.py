import requests

api_token = 'cqQkstGHxq4kb1wNhpbz1b11wh0byp'

api_url = 'https://10.22.65.1/api/v2/monitor/system/config/backup?scope=global&access_token=' + api_token

requests.packages.urllib3.disable_warnings() # Close https CA warning

data = requests.get(api_url, verify=False) # disable SSL https url verification

with open('C:/Users/user/Desktop/backups/api_backup.conf', 'wb') as f:
    for line in data:
        f.write(line)

#print(data.status_code) output status code
#print(data.text) Output config

