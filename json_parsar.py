__author__ = 'venkat'

import json
import httplib2

global h

h = httplib2.Http(".cache")
h.add_credentials('onos', 'rocks')

# Get the List of nodes available in the netw1rk
resp,content = h.request('http://127.0.0.1:8181/onos/v1/devices', 'GET')
nodes = json.loads(content.decode())
print(json.dumps(nodes))
print(json.dumps(nodes, sort_keys=True, indent=2))


