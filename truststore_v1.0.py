#from __future__ import print_function
import paramiko
import os

print ('-----------------------')
DEVICE = raw_input('Enter the device name: ')
print ('-----------------------')
USERNAME = raw_input('Enter _net username: ')
print ('-----------------------')
PASSWORD = raw_input('Enter _net password: ')
print ('-----------------------')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#ssh.connect('192.168.1.52', username='root', password='Labrat@123')
ssh.connect('%s' % DEVICE, username='%s' % USERNAME, password='%s' % PASSWORD)

print ('\n')
print ('\n')
print ('*************************************************')
print ('*************** Connected to %s ****************' %DEVICE)
print ('*************************************************')
print ('\n')
print ('\n')

print ('-----------------------')
BUNDLE_NAME = raw_input('Enter the bundle name: ')
print ('-----------------------')

a_stdin, a_stdout, a_stderr = ssh.exec_command('find / *.crt | grep \"%s\"' % BUNDLE_NAME)
a_output = a_stdout.readlines()
#a_output = a_output[:-1]

print ('\n')
print ('\n')
print ('*************************************************')
print ('*********** BUNDLE FOUND IN DEVICE!!! ***********')
print ('*************************************************')
print ('\n')
print ('\n')
print '\n'.join(a_output)
print ('\n')
print ('\n')

print ('-----------------------')
BNF = raw_input('Enter the actual bundle name found above:')
print ('-----------------------')

b_stdin, b_stdout, b_stderr = ssh.exec_command('openssl crl2pkcs7 -nocrl -certfile /config/filestore/files_d/Common_d/certificate_d/\:Common\:%s | openssl pkcs7 -print_certs -text -noout | grep -A 1 CN' % BNF)
b_output = b_stdout.readlines()
b_output = b_output[:-1]
print ('\n')
print ('\n')
print ('*************************************************')
print ('*********** CN FOUND IN BUNDLE!!! ***********')         
print ('*************************************************')
print ('\n')
print ('\n')
print '\n'.join(b_output)
print ('\n')
print ('\n')

print ('-----------------------')
CN = raw_input('Enter the CN: ')
print ('-----------------------')

c_stdin, c_stdout, c_stderr = ssh.exec_command('openssl crl2pkcs7 -nocrl -certfile /config/filestore/files_d/Common_d/certificate_d/\:Common\:%s | openssl pkcs7 -print_certs -text | grep -A100 CN=%s' % (BNF, CN))
c_output = c_stdout.readlines()
print ('\n')
print ('\n')
print ('*************************************************')
print ('************ PRINTING CERT BELOW!!! *************')             
print ('*************************************************')
print ('\n')
print ('\n')
c_output2 = '\n'.join(c_output)
c_output3 = c_output2[:-1]
print c_output3

ssh.close()

# Open a transport

host = "192.168.1.52"
port = 22
transport = paramiko.Transport((host, port))

# Auth

password = "Labrat@123"
username = "root"
transport.connect(username = username, password = password)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

# Download

filepath = '/config/filestore/files_d/Common_d/certificate_d/\:Common\:site1.lab.com.crt_194629_1'
localpath = '/tmp/site1.lab.com.crt_194629_1'
sftp.get(filepath, localpath)

sftp.close()
transport.close()
