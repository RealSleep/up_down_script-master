import pexpect
import sys

ip = {"sw_ab":"192.168.77.11", "sw_bc":"172.16.77.11", "r_ab":"192.168.77.1",
    "r_bc":"172.16.77.1", "r_abc":"10.10.10.1"}
tftp_server_ip = "192.168.0.100"
pw = "password"
enable_pw = "password"

for device_name in ip:
    child = pexpect.spawn('telnet %s' % (ip[device_name]))
    print ('connected %s' % (device_name))
    child.expect('Password:', timeout=120)
    child.sendline(pw)
    child.expect('>')
    child.sendline('enable')
    child.expect('Password:')
    child.sendline(enable_pw)
    child.expect('#')
    child.sendline('copy run tftp://%s/current_conf/%s-confg \n\n' % (tftp_server_ip, device_name))
    child.expect('#')
    print(child.before)
    print(child.after)
    print('done %s' % (device_name))
