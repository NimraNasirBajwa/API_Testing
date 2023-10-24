import http.client
import json
import ssl

"""SignUp"""
conn = http.client.HTTPSConnection("q-api.vdotok.dev", context=ssl._create_unverified_context())
payload = json.dumps({
    "first_name": "Nimra",
    "last_name": "Nasir",
    "email": "chat86@t3st.com",
    "password": "Admin1234$",
    "project_id": "269RVNOQ",
    "country" :"169"

})
headers = {
    'Content-Type': 'application/json'
}
conn.request("POST", "/AdminAPI/v0/SignUp", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# Extract relevant information from the response, if needed
response_json = json.loads(data)
email_code = response_json.get("email_code")

"""ValidateTenant"""
payload_for_second_api = {
    "verification_token": email_code,
     "email": "chat86@t3st.com",

}

payload_json_for_second_api = json.dumps(payload_for_second_api)
headers_for_second_api = {
    'Content-Type': 'application/json'
}

conn.request("POST", "/AdminAPI/v0/ValidateTenant", payload_json_for_second_api, headers_for_second_api)
res_second_api = conn.getresponse()

response_data_for_second_api = res_second_api.read()
print(response_data_for_second_api.decode("utf-8"))

# Extract relevant information from the response, if needed
response_json2 = json.loads(response_data_for_second_api)
auth_token = response_json2.get("auth_token")

"""AddTenantInformation"""
payload_for_Third_api = {
    "auth_token": auth_token,
    "organization_name": "vdotok",
    "business_type": "1"

}

payload_json_for_Third_api = json.dumps(payload_for_Third_api)
headers_for_Third_api = {
    'Content-Type': 'application/json'
}

conn.request("POST", "/AdminAPI/v0/AddTenantInformation", payload_json_for_Third_api, headers_for_Third_api)
res_Third_api = conn.getresponse()

response_data_for_Third_api = res_Third_api.read()
print(response_data_for_Third_api.decode("utf-8"))

"""AddProject"""
payload_for_Forth_api = {
    "auth_token": auth_token,
    "project_title": "vdotok",
    "role_id": "1"
}

payload_json_for_Forth_api = json.dumps(payload_for_Forth_api)
headers_for_Forth_api = {
    'Content-Type': 'application/json'
}

conn.request("POST", "/AdminAPI/v0/AddProject", payload_json_for_Forth_api, headers_for_Forth_api)
res_Forth_api = conn.getresponse()

response_data_for_Forth_api = res_Forth_api.read()
print(response_data_for_Forth_api.decode("utf-8"))
# Extract relevant information from the response, if needed
response_json3 = json.loads(response_data_for_Forth_api)
project_id = response_json3.get("project_id")

"""GetFreeMinutes"""
payload_for_Fifth_api = {
    "auth_token": auth_token,
    "project_id": project_id

}

payload_json_for_Fifth_api = json.dumps(payload_for_Fifth_api)
headers_for_Fifth_api = {
    'Content-Type': 'application/json'
}

conn.request("POST", "/AdminAPI/v0/GetFreeMinutes", payload_json_for_Fifth_api, headers_for_Fifth_api)
res_Fifth_api = conn.getresponse()

response_data_for_Fifth_api = res_Fifth_api.read()
print(response_data_for_Fifth_api.decode("utf-8"))

"""Login"""
payload_for_login_api = {
    "email": "chat86@t3st.com",
    "password": "Admin1234$",
    "project_id": project_id
}

payload_json_for_login_api = json.dumps(payload_for_login_api)
headers_for_login_api = {
    'Content-Type': 'application/json'
}

conn.request("POST", "/AdminAPI/v0/Login", payload_json_for_login_api, headers_for_login_api)
res_login_api = conn.getresponse()

response_data_for_login_api = res_login_api.read()
print(response_data_for_login_api.decode("utf-8"))
