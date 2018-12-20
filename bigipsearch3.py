#!/usr/bin/python 
#import ansible.runner
import ansible.playbook
import ansible.inventory
from ansible import utils

# creating the playbook instance to run, based on "test.yml" file
pb = ansible.playbook.PlayBook(
    playbook = "/home/shoaib/scripts/bigipsearch2.yaml",
    check=True
    )

# running the playbook
pr = pb.run() 
