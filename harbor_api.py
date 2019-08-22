import json
import requests
import functools


def _wrapper_harbor(func):
    """
    对所有请求harbor服务器资源的请求进行统一包装处理
    :param func:
    :return:
    """

    @functools.wraps(func)
    def __wrapper_harbor(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            raise e
        print(json.loads(result.text))
        if not result:
            raise Exception("请求harbor资源的方法必须带返回值")
        if result.status_code != 200:
            raise Exception(result.text)
        return json.loads(result.text)
    return __wrapper_harbor


class HarborTool(object):

    def __init__(self):
        self.headers = {
            'content-type': 'application/json',
            'Accept-Charset': 'UTF-8',
            'Accept': 'text/plain',
            'Authorization': "Basic YWRtaW46RGV2b3BzMjAxOQ=="
        }
        self.base_url = "https://10.176.140.38:5005/api"

    @_wrapper_harbor
    def test_repositories(self):
        url = self.base_url + "/repositories/ftest/vuetest/tags"
        return requests.get(url, verify=False, headers=self.headers)

    @_wrapper_harbor
    def test_search(self):
        url = self.base_url + "/search"
        params = {'q': 'ftest/sockettest'}
        return requests.get(url, params=params, verify=False, headers=self.headers)

    @_wrapper_harbor
    def get_projects(self):
        url = self.base_url + "/projects"
        params = {"name": "ftest"}
        return requests.get(url, params=params, verify=False, headers=self.headers)


harbor_tool = HarborTool()
