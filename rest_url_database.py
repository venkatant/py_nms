__author__ = 'venkat'

base_url = 'http://127.0.0.1:8181/'

'''
Specific URL's
'''
# Get the list of Switches present in the network
REST_URL_FOR_NODE = base_url + 'onos/v1/devices'

# Get the individual Link status connected to a Switch
REST_URL_FOR_LINK = base_url + 'onos/v1/links?device='

# Get the individual Flows installed in a network
# REST_URL_FOR_FLOW = base_url + 'controller/nb/v2/statistics/default/flow'

# Get the individual Flows installed in a switch
REST_URL_FOR_FLOW = base_url + 'controller/nb/v2/statistics/default/flow/node/OF/'

# Get the individual port statistics of a switch
REST_URL_FOR_PORT = base_url + 'onos/v1/devices/'

# Get the list of hosts connected to each switch
REST_URL_FOR_HOST = base_url + 'onos/v1/hosts/'

#REST_URL_FOR_PORT = base_url + 'controller/nb/v2/statistics/default/port'
