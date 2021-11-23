# Step 1: get needed variables 
appsettings = {}
with open('appsettings.json', 'r',) as f:
    import json
    appsettings = json.load(f)

resource = appsettings.get('Resource')
api_version = appsettings.get('ApiVersion')
tenant_id = appsettings.get('TenantId')
client_id = appsettings.get('ClientId')
client_secret = appsettings.get('ClientSecret')


import requests
import json

# Step 2: get the authentication endpoint from the discovery URL
wellknown_information = requests.get(f'{resource}/identity/.well-known/openid-configuration')
token_url = json.loads(wellknown_information.content)["token_endpoint"]

# Step 3: use the client ID and Secret to get the needed bearer token
token_information = requests.post(token_url,data={'client_id': client_id,'client_secret': client_secret,'grant_type': 'client_credentials'})
token = json.loads(token_information.content)["access_token"]

# Step 4: test token by calling the base tenant endpoint 
msg_headers= {"Authorization": f'Bearer {token}'}
test = requests.get(f'{resource}/api/{api_version}/Tenants/{tenant_id}', headers=msg_headers)

# test it by making sure we got a valid http status code  
assert test.status_code >= 200 and test.status_code < 300