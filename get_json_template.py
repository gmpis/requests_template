import requests
import os
# import pprint

base_url = "https://api.openweathermap.org/data/2.5/weather"
m_headers = {"User-Agent": "My Test Weather App"}

# SOS!!! DO NOT commit API keys on (public) repos, AND IF YOU DO, REVOKE THEM IMMEDIATELY,
# to set environment variables use: export M_API_KEY=000000
m_API_Key = os.getenv("M_API_KEY", "API_KEY_4_TESTING")  # read key from env vars, use the default val only for testing locally
m_params = {"q": "Ioannina,GR", "appid": m_API_Key, "units": "metric"}  # ?key=value
m_timeout = 1  # in sec


m_resp = requests.get(base_url, headers=m_headers, params=m_params, timeout=m_timeout)

if m_resp.status_code == requests.codes.ok:
    # print(m_resp.headers)  # class ... 'CaseInsensitiveDict'
    # print(m_resp.text)

    m_resp_json = m_resp.json()  # class 'dict'

    # pr_pr = pprint.PrettyPrinter(indent=4)
    # pr_pr.pprint(m_resp_json)  # pretty print response data
    # to validate and pretty print the contents of a json file in disk, from shell run:
    # python3 -m json.tool file_name.json

    current_weather_desc = m_resp_json["weather"][0]["description"]
    print("Weather: " + current_weather_desc)
    # do something with the data here ...


else:
    print("Sorry something went wrong...")
    print("Status code: " + str(m_resp.status_code))

print("Done, exiting now ...")