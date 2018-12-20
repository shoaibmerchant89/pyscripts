print ('\n')
print("====Welcome to BIGIP Search tool====")
#search = open('subnets.txt','r')
#print '\n'
#userinput = input(str('Type the subnets to search: '))
# 1.1 searchlist should be updated with the subnets to search for
searchlist = ['address 172.16.5.10','address 172.16.5.11']
search = str(searchlist)
print ('\n')
print ('The following subnets will be searched: ')
print (search)

# 1.2 creating empty list that will be populated based on output of 1.3
sloughpools = []
print ('\n')

# 1.3 searching pool.txt file using the searchlist confgured in step 1.1 as an input
with open('pool.txt', 'r') as fp:
    for pool in fp:
        for ip in searchlist:
        	if ip in pool:
        			# 1.4 capturing search result as a 'list' which will serve as an input in step 1.7
               		sloughpools.append(pool.split()[2])

print '====Following are the Pools in Slough===='
print ('\n')
# 1.5 printing search result list for information
print (sloughpools)
print ('\n')

# 1.6 creating empty list that will be populated based on output of 1.8
sloughvips = []

# 1.7 searching pool.txt file using the sloughpools list as an input
with open('virtual.txt', 'r') as fv:
    for vip in fv:
        for pool in sloughpools:
                if pool in vip:
        				# 1.8 capturing search result as a 'list' which will serve as an output in step 1.9
                        sloughvips.append(vip.split()[2])

print ('====Following are the VIPs in Slough====')
print ('\n')
# 1.9 printing search result list for information
print (sloughvips)
print ('\n')

