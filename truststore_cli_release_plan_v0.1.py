import os
path = os.path.join(os.path.expanduser('~'), 'Desktop')

var0 = crt.Dialog.Prompt('Enter change number: ')
var1 = crt.Dialog.Prompt('Release plan created by: ')
var2 = crt.Dialog.Prompt('Incident number: ')
var3 = crt.Dialog.Prompt('ITSI name: ')
var4 = crt.Dialog.Prompt('Device Name: ')


#f = open('/home/shoaib/Desktop/file1.txt', 'w')
#f.write(print('My name is {first} {last}')

def func1():
    print >> f, '************************************************'
    print >> f, '! Change Number   : {0}'.format(var0)
    print >> f, '! Created By      : {0}'.format(var1)
    print >> f, '! Incident Number : {0}'.format(var2)
    print >> f, '! ITSI Name       : {0}'.format(var3)
    print >> f, '! Device Name     : {0}'.format(var4)
    print >> f, '************************************************\n'

with open('{path}\\release_plan_{name}.txt'.format(path=path, name=var0), 'w') as f:
    func1()

ICON_INFO = 64                  # displays "info" icon.
path_info = crt.Dialog
path_info.MessageBox('Release plan saved at {0}\\release_plan_{1}.txt'.format(path, var0), "Info", ICON_INFO)
