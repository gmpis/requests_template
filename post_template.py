import requests

base_url = "https://httpbin.org/anything"

m_headers = {"User-Agent": "My Test App"}
m_params = {"key": "value"}  # ?key=value
m_timeout = 1  # in sec

m_payload = {"Hello": "World!", "Here": "Request Body"}  # request body goes here

# m_resp = requests.post(base_url, headers=m_headers, params=m_params, data=m_payload, timeout=m_timeout)
m_resp = requests.post(base_url, headers=m_headers, params=m_params, json=m_payload, timeout=m_timeout)  # alt: data=m_payload,

if m_resp.status_code == requests.codes.ok:
    print("POST request was successful")
    # print(m_resp.headers)  # class ... 'CaseInsensitiveDict'
    print(m_resp.text)

    # other ways to access Response content
    # print(m_resp.content)  # for non text-requests, binary response
    # print(m_resp.json())


else:
    print("Sorry something went wrong...")
    print("Status code: " + str(m_resp.status_code))

print("Done, exiting now ...")