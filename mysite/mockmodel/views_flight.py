# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 18:56
# @Author  : huangkaiding
import re

from mockmodel.mock_flight import policy_confirmation, policy_cancellation, policy_printing

pat = '<RequestType>(.*?)</RequestType>'


def policy_confirmation_api(request):
    if request.method == 'POST':
        body = request.body
        print(body)
        result_type = re.compile(pat, re.S).findall(str(body))
        print(result_type[0])
        if result_type[0] == '0002':
            return policy_confirmation()
        elif result_type[0] == '0004':
            return policy_cancellation()
        elif result_type[0] == '0006':
            return policy_printing()
