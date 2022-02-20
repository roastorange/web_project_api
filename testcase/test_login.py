import jsonpath
import pytest

from common.handle_logging import log
from api.login_api import login_api_res
from run import cmd_env

if cmd_env == 'dev':  # 分环境导入用例数据
    from data.dev_data.case_data import Login
else:
    from data.pro_data.case_data import Login


class TestLogin:

    @pytest.mark.parametrize("case_data", Login.case_data)
    def test_login(self, case_data):
        res = login_api_res(case_data["case_data"])
        expected = case_data["expected"]
        try:
            assert jsonpath.jsonpath(res, "$..code")[0] == expected["code"]
            assert jsonpath.jsonpath(res, "$..msg")[0] == expected["msg"]
        except AssertionError as e:
            log.error("用例--{}--执行未通过".format(case_data["case_title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过".format(case_data["case_title"]))
