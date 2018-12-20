import os
import re
import sys

path = os.path.join(os.path.expanduser('~'), 'Desktop')

device = crt.Dialog.Prompt('Enter the device name: ')
username = crt.Dialog.Prompt('Enter _net username: ')


def login():
    password = crt.Dialog.Prompt('Enter _net password: ')
    cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M SHA1 %s" % (username, password, device)
    crt.Session.Connect(cmd)


login()

# *********** CONNECTED TO DEVICE!!! ***********

crt.Screen.WaitForString("config #")
ICON_INFO = 64                  # displays "info" icon.
crt.Dialog.MessageBox('Connected to {0}!'.format(device), "Info", ICON_INFO)

# *********** FIND BUNDLE ***********

bundle_name = crt.Dialog.Prompt('Enter the bundle name: ')
crt.Screen.Send('find /config/filestore/files_d/Common_d/certificate_d/ '
                '*.crt | grep \"{0}\"'.format(bundle_name) + '\n')

# *********** BUNDLE FOUND IN DEVICE!!! ***********

crt.Screen.WaitForString("No such file or directory")
ICON_INFO = 64                  # displays "info" icon.
crt.Dialog.MessageBox('Bundle found in {0}!'.format(device), "Info", ICON_INFO)
crt.Dialog.MessageBox('Copy the bundle name starting after :Common:', "Info", ICON_INFO)

# *********** ENTER THE ACTUAL BUNDLE NAME ***********

crt.Screen.WaitForCursor(100)
crt.Screen.WaitForCursor(100)
actual_name = crt.Dialog.Prompt('Enter the actual bundle name found above:')
crt.Screen.Send('openssl crl2pkcs7 -nocrl -certfile /config/filestore/files_d/'
                'Common_d/certificate_d/\:Common\:{0} | openssl pkcs7 -print_certs '
                '-text -noout | grep -A 1 CN'.format(actual_name) + '\n')

# *********** Number of CN to search in the bundle? ***********

cn_nums = crt.Dialog.Prompt('Enter the number of CNs to search in bundle {0}'.format(actual_name))
cn_nums_int = int(cn_nums)


def func2():

    # *********** CN FOUND IN BUNDLE!!! ***********
    # crt.Screen.WaitForString("config #")
    # crt.Screen.WaitForCursor(100)
    # ICON_INFO = 64                  # displays "info" icon.
    # crt.Dialog.MessageBox('CN found in {0}'.format(actual_name), "Info", ICON_INFO)
    # crt.Dialog.MessageBox('Copy the CN now')

    # *********** ENTER THE CN ***********

    crt.Screen.WaitForString("config #")
    crt.Screen.WaitForCursor(100)
    cn = crt.Dialog.Prompt('Enter the CN: ')
    crt.Screen.Send('openssl crl2pkcs7 -nocrl -certfile /config/filestore/'
                    'files_d/Common_d/certificate_d/\:Common\:{0} | openssl '
                    'pkcs7 -print_certs -text | grep -A100 CN={1}'.format(actual_name, cn) + '\n')

    crt.Screen.WaitForString('openssl')
    result = crt.Screen.ReadString('config #')

    global i

    with open('{0}\\old_certs\\cert_{1}_{2}.txt'.format(path, i, cn), 'w+') as fi:
        for new_result in re.findall('-----BEGIN CERTIFICATE-----(.*?)-----END CERTIFICATE-----', result, re.S):
            print >> fi, ('-----BEGIN CERTIFICATE-----' + new_result + '-----END CERTIFICATE-----\n')


for i in range(0,cn_nums_int,1):
    func2()
