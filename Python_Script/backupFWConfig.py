from netmiko import ConnectHandler
import datetime

# Firewall host that we want to SSH into:
my_fw = {'host': 'TP-FH4F-FW-01',
         'device_type': 'fortinet',
         'ip': '10.22.65.1', # Firewall IP accessed by this machine
         'username': 'frank', # as created on the firewall
         'password': '02021111'}

net_connect = ConnectHandler(**my_fw) # Create connect handler object

output = net_connect.send_command('show full-configuration') # SSH and send command to the firewall and save the output

current_time = datetime.datetime.today().strftime('%Y_%b_%d') # This is to add to the naming of the file

# Create a file and write the output on it. Make sure the directory is valid on this machine:
with open('C:/Users/user/Desktop/backups/' + str(my_fw['host']) + '_' + str(current_time) + '.conf', 'w') as f:
    for line in output:
        f.write(line)
net_connect.disconnect() #Close SSH session
