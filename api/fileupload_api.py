from run import cmd_env
from common.handle_config import conf
import requests


def fileupload_api_res(case_data):
    if cmd_env == "dev":
        url = conf.get("dev", "public_url") + "/file/upload"
        headers = {"X-Lemonban-Media-Type": "lemonban.v1"}
        data = case_data
    else:
        url = conf.get("pro", "public_url") + "/file/upload"
        headers = {"X-Lemonban-Media-Type": "lemonban.v1"}
        data = case_data
    res = requests.request(method="POST", url=url, headers=headers, files=data).json()
    return res






