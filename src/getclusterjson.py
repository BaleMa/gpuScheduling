import json
import requests
import sys

print ("please input job name")
#print "args",sys.argv

#jobname = sys.argv[1]
host1 = 'http://192.168.2.210'
host2 = 'http://192.168.2.216'
getnode = '/ws/v1/cluster/nodes'
yarnport = ':8088'
paiport = ':9186'
posttoken = '/api/v1/token'
#url = 'http://192.168.2.210/rest-server/api/v1/jobs/' + jobname

logdata = {
  "username": "mahaifeng",
  "password": "mahaifeng",

}

totalurl = host1+paiport+posttoken
print(totalurl)
logrepeonse = requests.post(totalurl, data = logdata)
print(logrepeonse.status_code)
print(logrepeonse.text)

if logrepeonse.status_code == 401:
    exit(0)
r = requests.get(host1+yarnport+getnode)
print (r.status_code)
if r.status_code == 200:
    print(r.text)
    data = json.loads(r.text)
    #print data['taskRoles']['mnist']['taskStatuses'][0]['containerIp'] + ':9100'

    #print data['taskRoles']['mnist']['taskStatuses']

    #for index in range(len(data.taskRoles[taskRole].taskStatuses))
print ( data )
'''
    for taskRole in data['taskRoles']:
        print taskRole['taskRoles']
        for  taskStatuse in taskRole['taskRoles']['taskStatuses']:
            for ContainerIp in data['taskRoles'][taskRole]['taskStatuses'][taskStatuse]['containerIp']:
                print data['taskRoles'][taskRole]['taskStatuses'][taskStatuse]['containerIp'][ContainerIp]
'''
