import subprocess
import os

network_status_cmd = "ip a | grep ens192"
open_ports_cmd = "ss -tulwn | grep LISTEN | awk '{print $5}'"
firewalld_status_cmd = "systemctl status firewalld | grep active"
apache_restart_cmd = "systemctl restart httpd"
#********************************************************
test1 = subprocess.Popen([network_status_cmd], stdout=subprocess.PIPE,shell=True)
network_status = test1.stdout.read().strip()

test2 = subprocess.Popen([open_ports_cmd], stdout=subprocess.PIPE,shell=True)
open_ports = test2.stdout.read().strip()

test3 = subprocess.Popen([firewalld_status_cmd], stdout=subprocess.PIPE,shell=True)
firewalld_status = test3.stdout.read().strip()

#********************************************************
"""
with open('/etc/httpd/conf/httpd.conf','a+') as f:
  #Checking whether or not the apache version is hidden 
   if 'ServerSignature Off' and 'ServerTokens Prod' in f.read() :
    print " The apache version is hidden "
   else:
    print " The apache version is not hidden, it will be added now "
    f.write('ServerSignature OFF\nServerTokens Prod')
    
  #Checking if directory listing is turned off
#   if 'Options -Indexes' in f.read() :
#      print "The directory listing is off, good to go"
#   else:
#       lines = f.readline()
#       print       

"""
f =  open('/etc/httpd/conf/httpd.conf','r+')
  #Checking whether or not the apache version is hidden
cur_line = f.readlines()
print(cur_line[0])
for i in range(0,len(cur_line)):
    direc = '<Directory "/var/www/html/">'
    if direc in cur_line[i]: 
        if "Options -Indexes" in cur_line[i+1]:
            print("Directory Lisitng is turned off")
            break
        elif "Options" in cur_line[i+1]:
            cur_line += " -Indexes"
            print ("Directory Listing is not off, it will now be turned off")
            break
print(cur_line[0])
f.writelines(cur_line)
#print("Network status:\n " + network_status + "\n")
#print("Open ports:\n " + open_ports+ "\n")
#print ("Status of firewalld\n: " + firewalld_status+ "\n")
