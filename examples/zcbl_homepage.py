#!/usr/bin/python
# encoding: utf-8

"""
@auth: zhaopan
@time: 2018/4/11 09:58
"""
from proxy2 import *

class ProxyZCBLHandler(ProxyRequestHandler):

    def request_handler(self, req, req_body):
        pass

    def response_handler(self, req, req_body, res, res_body):
        if req.path == 'https://bjjj.zhongchebaolian.com/app_web/jsp/homepage.jsp':
            import requests
            res2 = requests.get('https://qdota.com/bjjj/homepage_chunnel.jsp')
            return res2.text


if __name__ == '__main__':
    test(HandlerClass=ProxyZCBLHandler)
