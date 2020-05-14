import requests
import re
import urllib3
import base64

WEB_URL = "https://10.0.129.100"
USERNAME = "admin@alauda.io"
PASSWORD = "password"
PROXY_SERVER = "http://139.186.2.80:37491"


def get_token(idp_name='local', username=USERNAME, password=PASSWORD):
    proxy = {"https": "http://139.186.2.80:37491"}
    url = WEB_URL + "/console-acp/api/v1/token/login"
    urllib3.disable_warnings()
    headers = {"Referer": "{url}/console-acp".format(url=WEB_URL)}
    r = requests.get(url, verify=False, timeout=15, proxies=proxy, headers=headers)
    auth_url = r.json()["auth_url"]
    auth_path = '/'.join(auth_url.split("/")[-2:])
    auth_url = WEB_URL + '/' + auth_path
    r = requests.get(auth_url, verify=False, proxies=proxy)
    content = r.text
    print(content)
    req = re.search('req=[a-zA-Z0-9]{25}', content).group(0)[4:]
    url = WEB_URL + "/dex/auth/{}?req=".format(idp_name) + req
    # generate connectorID
    requests.get(url, verify=False, timeout=10, proxies=proxy)
    # login acp platform
    params = {"login": username, "encrypt": str(base64.b64encode(password.encode('utf-8')), "utf8")}

    response = requests.post(
        url, params=params, verify=False, timeout=10, proxies=proxy)
    content = response.history[1].text

    code = re.search('[a-zA-Z0-9]{25}', content).group(0)
    url = WEB_URL + "/console-acp/api/v1/token/callback?code={}&state=alauda-console".format(
        code)

    r = requests.get(url, verify=False, proxies=proxy, headers=headers)
    ret = r.json()
    token = ret['id_token']
    return token


TOKEN = get_token()
