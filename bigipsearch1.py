print '\n'
print("====Welcome to BIGIP Search tool====")
#search = open('subnets.txt','r')
#print '\n'
#userinput = input(str('Type the subnets to search: '))
searchlist = ['address 172.16.4','address 10.10.5','address 172.16.8']
search = str(searchlist)
print '\n'
print 'The following subnets will be searched: '
print (search)

sloughpools = []

print ('\n')

with open('pool.txt', 'r') as fp:
    for pool in fp:
        for ip in searchlist:
        	if ip in pool:
               		sloughpools.append(pool.split()[2])

print '====Following are the Pools in Slough===='
print '\n'
print sloughpools

sloughvips = []
print '\n'

with open('virtual.txt', 'r') as fv:
    for vip in fv:
        for pool in sloughpools:
                if pool in vip:
                        sloughvips.append(vip.split()[2])

print '====Following are the VIPs in Slough===='
print '\n'
print sloughvips
print '\n'
