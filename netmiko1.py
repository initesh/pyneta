from netmiko import ConnectHandler
from getpass import getpass 
import os 
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
nxos1 = {
    "host" : 'nxos1.lasthop.io',
    "username" : 'pyclass',
    "password" : password,
    "device_type" : 'cisco_nxos',
    # "session_log": 'my_session.txt',
}
nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}
for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_command("Show version", expect_string=r'#')
    print (output)

