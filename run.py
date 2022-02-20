import argparse
import os
import pytest

"""
实现命令行传参来选取dev线下环境还是pro生产环境的测试
"""
# 创建一个解析对象
parser = argparse.ArgumentParser(description="choose cmd params")
# 向该对象中添加你要关注的命令行参数和选项（通过-e参数指定运行环境，默认是dev环境）
parser.add_argument('-e', '--env', default='dev')
# 进行解析
args = parser.parse_args()

cmd_env = args.env  # 其他模块通过导入cmd_env后进行条件判断是dev还是pro,以便测试数据等的选取

pytest.main(['-s', '--alluredir=allure_report'])
# os.system('allure serve allure_report')
