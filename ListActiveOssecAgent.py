import json
import requests # Install request: pip install requests

# Configuration
base_url = 'https://127.0.0.1:55000'
auth = requests.auth.HTTPBasicAuth('foo', 'bar')
verify = False

# Request
url = '{0}{1}'.format(base_url, "/agents?status=Active")
r = requests.get(url, auth=auth, params=None, verify=verify)
print(json.dumps(r.json(), indent=4, sort_keys=True))
print("Status: {0}".format(r.status_code))
