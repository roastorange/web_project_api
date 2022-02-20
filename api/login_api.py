import requests
from run import cmd_env
from common.handle_config import conf


def login_api_res(case_data):
    if cmd_env == "dev":
        url = conf.get("dev", "public_url") + "/user/login"
        headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
        data = case_data
    else:
        url = conf.get("pro", "public_url") + "/user/login"
        headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
        data = case_data
    res = requests.request(method="POST", url=url, headers=headers, json=data).json()
    return res
