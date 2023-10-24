import http.client
import json
import ssl
from Login import email_code

conn = http.client.HTTPSConnection("q-api.vdotok.dev", context=ssl._create_unverified_context())
payload = json.dumps({
{
    "auth_token":"auth_token",
    "organization_name":"vdotok",
    "business_type": "1"
}
})
headers = {
    'Content-Type': 'application/json'
}
conn.request("POST", "/AdminAPI/v0/ValidateTenant", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

