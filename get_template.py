import requests

base_url = "https://www.google.com"

m_user_agent = "My Test App"  # use something more descriptive
# eg Firefox: "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0"
m_headers = {"User-Agent": m_user_agent}

m_params = {"key": "value"}  # ?key=value
m_timeout = 1  # in sec


m_resp = requests.get(base_url, headers=m_headers, params=m_params, timeout=m_timeout)
m_final_url = m_resp.url
print(m_final_url)
print(m_resp.status_code)


if m_resp.status_code == requests.codes.ok:
    print("GET request was successful")
    # print(m_resp.cookies)
    print(m_resp.headers)  # class ... 'CaseInsensitiveDict'
    print(m_resp.text)

    # other ways to access Response content
    # print(m_resp.content)  # for non text-requests, binary response
    # print(m_resp.json())


else:
    print("Sorry something went wrong...")
    print("Status code: " + str(m_resp.status_code))

print("Done, exiting now ...")