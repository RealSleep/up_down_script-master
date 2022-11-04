import wexpect 

password = 'password'

tftp__server = '192.168.77.10'

conf_type = ["current","final","start"]

ip = {'sw_ab':['192.168.77.11'], 'sw_bc':['172.16.77.11'], 
    'r_ab':['192.168.77.1'], 'r_bc':['172.16.77.1'], 'r_abc':['10.10.10.1']}

for device_name in ip:
    child = wexpect.spawn('telnet %s' % (ip[device_name][0]))
    print ('Connected %s' % (device_name)) 
    child.expect('Password:')
    child.sendline(password)
    child.expect('>')
    child.sendline('en')
    child.expect('Password:')
    child.sendline('password')
    child.expect('#')
    from_dir = "tftp://%s/%s/%s-confg.config" % (tftp__server, conf_type[1], device_name)
    to_dir = "run"
    child.sendline('copy %s %s \n\n' % (from_dir, to_dir))
    print (child.before)
    print (child.after)
    print ('Done')