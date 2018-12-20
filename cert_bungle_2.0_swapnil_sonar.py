import paramiko

import time

import os

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect('192.168.0.4', port=22, username='root', password='default')

print("successful connection")

channel = ssh_client.invoke_shell()

number = int(input("Please enter the number of certificates you want to change(e.g. 1,2 or 3): " + "\n"))

if number == 1:

    old_cert_bundle = input("Please enter the name of Old cert bundle: " + "\n")

    new_bundle = input("Please enter the name of new bundle: " + "\n")

    SN1 = input("Please enter the serial number of cert which you want to delete: " + "\n")

    channel.send(
        'openssl crl2pkcs7 -nocrl -certfile /config/filestore/files_d/Common_d/certificate_d/:Common:' + old_cert_bundle + ".*" + " | openssl pkcs7 -print_certs -text | sed -r '/" + SN1 + "/,/END CERTIFICATE/d' >> /var/tmp/temp-1.crt\n")

    time.sleep(1)

    server_ssl = input("Please enter the name of server-ssl profile\n")

    channel.send("tmsh install /sys crypto cert " + new_bundle + ".crt from-local-file /var/tmp/temp-1.crt\n")

    time.sleep(1)

    channel.send('rm -rf /var/tmp/temp-1.crt\n')

    time.sleep(1)







elif number == 2:

    old_cert_bundle = input("Please enter the name of Old cert bundle: " + "\n")

    new_bundle = input("Please enter the name of new bundle: " + "\n")

    SN1 = input("Please enter the first serial number: " + "\n")

    channel.send(
        'openssl crl2pkcs7 -nocrl -certfile /config/filestore/files_d/Common_d/certificate_d/:Common:' + old_cert_bundle + ".*" + " | openssl pkcs7 -print_certs -text | sed -r '/" + SN1 + "/,/END CERTIFICATE/d' >> /var/tmp/temp-1.crt\n")

    time.sleep(1)

    SN2 = input("Please enter the second serial number: " + "\n")

    channel.send(
        "openssl crl2pkcs7 -nocrl -certfile /var/tmp/temp-1.crt | openssl pkcs7 -print_certs -text | sed -r '/" + SN2 + "/,/END CERTIFICATE/d' >> /var/tmp/temp-2.crt\n")

    time.sleep(1)

    server_ssl = input("Please enter the name of server-ssl profile\n")

    channel.send("tmsh install /sys crypto cert " + new_bundle + ".crt from-local-file /var/tmp/temp-2.crt\n")

    time.sleep(1)

    channel.send('rm -rf /var/tmp/temp-1.crt\n')

    channel.send('rm -rf /var/tmp/temp-2.crt\n')

    time.sleep(1)







elif number == 3:

    old_cert_bundle = input("Please enter the name of Old cert bundle: " + "\n")

    new_bundle = input("Please enter the name of new bundle: " + "\n")

    SN1 = input("Please enter the first serial number: " + "\n")

    channel.send(
        'openssl crl2pkcs7 -nocrl -certfile /config/filestore/files_d/Common_d/certificate_d/:Common:' + old_cert_bundle + ".*" + " | openssl pkcs7 -print_certs -text | sed -r '/" + SN1 + "/,/END CERTIFICATE/d' >> /var/tmp/temp-1.crt\n")

    time.sleep(1)

    SN2 = input("Please enter the second serial number: " + "\n")

    channel.send(
        "openssl crl2pkcs7 -nocrl -certfile /var/tmp/temp-1.crt | openssl pkcs7 -print_certs -text | sed -r '/" + SN2 + "/,/END CERTIFICATE/d' >> /var/tmp/temp-2.crt\n")

    time.sleep(1)

    SN3 = input("Please enter the third serial number: " + "\n")

    channel.send(
        "openssl crl2pkcs7 -nocrl -certfile /var/tmp/temp-2.crt | openssl pkcs7 -print_certs -text | sed -r '/" + SN3 + "/,/END CERTIFICATE/d' >> /var/tmp/temp-3.crt\n")

    time.sleep(1)

    server_ssl = input("Please enter the name of server-ssl profile\n")

    channel.send("tmsh install /sys crypto cert " + new_bundle + ".crt from-local-file /var/tmp/temp-3.crt\n")

    time.sleep(1)

    channel.send('rm -rf /var/tmp/temp-1.crt\n')

    channel.send('rm -rf /var/tmp/temp-2.crt\n')

    channel.send('rm -rf /var/tmp/temp-3.crt\n')

    time.sleep(1)





else:

    print("*****************************************************************")

    print("Please enter the valid number. you can change upto 3 certificates.")

    print("Please enter 1, 2 or 3")

    print("*****************************************************************")

channel.send("tmsh modify ltm profile server-ssl " + server_ssl + " ca-file " + new_bundle + ".crt\n")

time.sleep(1)

channel.send("tmsh list ltm profile server-ssl " + server_ssl + "\n")

ssh_client.close()

output = channel.recv(65535)

print(output)

